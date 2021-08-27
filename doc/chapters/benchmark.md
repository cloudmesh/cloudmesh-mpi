## Benchmarks

This sectiion is in more detail published at this
[link](https://laszewski.medium.com/easy-benchmarking-of-long-running-programs-82059d9c67ce).
If the link does not work use this
[Link](https://laszewski.medium.com/easy-benchmarking-of-long-running-programs-82059d9c67ce?sk=7ed2ca2dacf7253c41e7ca4e180e2e1a).

### Introduction

We explain how we can manage long-running benchmarks. There are many useful
tools to conducting benchmarks such as `timeit`, `cprofile`, `line_profiler`,
and `memry_profiler` to name only a few. However, we present here an extremely
easy way to obtain runtimes while dealing with the fact that they could run
multiple hours or even days and could cause your system to crash. Hence if we
wor to run it in a single program it will lead to a loss of information and
many hours of unneeded replication.

We use and demonstrate how we achieve this with a simple StopWatch, creation of
shell scripts and even the integration of Jupyter notebooks.

### Prerequisites

As usual, we recommend that you use a virtual env. dependent on where your python
3 is installed, please adapt accordingly (python, or python3). Also, test out
which version of python you have. On Windows, we assume you have gitbash
installed and use it.

```bash
$ python3 -- version   # observe that you have the right version
$ python3 -m venv ~/ENV
$ source ~/ENV3/bin/activate
# or for Windows gitbash
# source ~/ENV3/Scripts/activate
```

### System Parameters

It is essential that we benchmark programs to show their effect on the time
consumed to obtain the results. Various factors play a role. This includes the
number of physical computers involved, the number of processors on each
computer, the number of cores on each computer, and the number of threads for
each core. We can summarise these parameters as a vector such as 

```
S(N, p, c, t)
```

Where 

* `S` = is a placeholder for the system
* `N` = Number of computers or nodes
* `p` = Number of processors per node
* `c` = Number of cores per processor
* `t` = Number of threads per processor

In some cases, it may be more convenient to specify the total values as

```
S^T(N, N*p, N*p*c, N*p*c*t)
```

and 

* `T` = indicates total


In the case of heterogeneous systems, we define multiple such vectors to form a 
list of vectors. 

For the rest of the section, we assume the system is homogeneous.


#### System Information

Cloudmesh provides an easy command that can be used to obtain information to
derive these values while using the command. However, it only works if the
number of processors on the same node is 1.

```
pip install cloudmesh-cmd5
cms help    # call it after the install as it sets some defaults
cms sysinfo 
```

The output will be looking something like 

```
+------------------+----------------------------------------------+
| Attribute        | Value                                        |
+------------------+----------------------------------------------+
| cpu              | Intel(R) Core(TM) i7-7920HQ CPU @ 3.10GHz    |
| cpu_cores        | 4                                            |
| cpu_count        | 8                                            |                                                    
| cpu_threads      | 8                                            |                                                    
| frequency        | scpufreq(current=3100, min=3100, max=3100)   |                                                    
| mem.active       | 5.7 GiB                                      |                                                    
| mem.available    | 5.8 GiB                                      |                                                    
| mem.free         | 96.7 MiB                                     |                                                    
| mem.inactive     | 5.6 GiB                                      |                                                    
| mem.percent      | 63.7 %                                       |                                                    
| mem.total        | 16.0 GiB                                     |                                                    
| mem.used         | 8.2 GiB                                      |                                                    
| mem.wired        | 2.4 GiB                                      |                                                    
| platform.version | 10.16                                        |                                                    
| python           | 3.9.5 (v3.9.5:0a7dcbdb13, ...)               |                                               
| python.pip       | 21.1.2                                       |                                                    
| python.version   | 3.9.5                                        |                                                   
| sys.platform     | darwin                                       |                                                    
| uname.machine    | x86_64                                       |                                                    
| uname.node       | mycomputer                                   |                                                    
| uname.processor  | i386                                         |
| uname.release    | 20.5.0                                       |                                                    
| uname.system     | Darwin                                       |                                                    
| uname.version    | Darwin Kernel Version 20.5.0: ....           |
| user             | gregor                                       |                                                      
+------------------+----------------------------------------------+
```

To obtain the vectors you can say

```
cms sysinfo -v
cms sysinfo -t
```

where `-v` specifies the vector and `-t` the totals.  Knowing these values will
help you structure your benchmarks.

#### Parameters

A benchmark is typically run while iterating over a number of parameters and
measuring some system parameters that are relevant for the benchmark, such as
the runtime of the program or application.

Let us assume our application is called `f` and its parameters are `x` and `y`

To create benchmarks over x and y we can generate them in various ways. 

#### Python only solution

For all programs, we will store the output of the benchmarks in a directory called 
`benchmark`. Please create it.

```bash
$ mkdir benchmark
```

you may be able to run your benchmark simply as a loop this is especially
the case for smaller benchmarks.

```python
import pickle
from cloudmesh.common.StopWatch import StopWatch

def f(x,y, print_benchmark=False, checkpoint=True):
    # run your application with values x and y
    print (f"Calculate f({x},{y})")
    StopWatch.start(f"f{x},{y}")
    result = x*y
    StopWatch.stop(f"f{x},{y}")
    if print_benchmark:
        StopWatch.benchmark()
    if checkpoint:
        pickle.dump(result, open(f"benchmark/f-{x}-{y}.pkl", "wb" ))  
    return result

x_min = 0
x_max = 2
d_x = 1
y_min = 0
y_max = 1
d_y = 1
for x in range(x_min, x_max, dx):
    for y in range(y_min, y_max, dy):
        # run the function with parameters
        result = f(x ,y, print_benchmark=True)
```

#### Script solution

In some cases, the functions themselves may be large and in case the benchmark
causes a crash of the python program executing it we would have to start over.
In such cases, it is better to develop scripts that take parameters so we can
execute the program through shell scripts and exclude those that fail.

For this, we rewrite the python program via command-line arguments that we pass along.

```python
# stored in file f.py
import click

@click.command()
@click.option('--x', default=20, help='The x value')
@click.option('--x', default=40, help='The y value')
@click.option('--print_benchmark', default=True, help='prints the benchmark result')
@click.option('--checkpoint', default=True, help='Creates a checkpoint')
f(x,y, print_benchmark=False, checkpoint=True):
    ... see previous program
    return result

if __name__ == '__main__':
    f()
```

Now we can run this program with 

```python
$ python f.py --x 10 --y 5
```

To generate now the different runs from the loop we can do it either via
Makefiles or write a program creating commands where we produce a script listing
each invocation. Let us call this program `sweep-generator.py`.


```python
x_min = 0
x_max = 2
d_x = 1
y_min = 0
y_max = 1
d_y = 1
for x in range(x_min, x_max, dx):
    for y in range(y_min, y_max, dy):
        print (f"cms banner f({x}, {y}; " 
               f"python f.py --x {x} --y {y}")
```

The result will be 

```
cms banner f(0,0); python f.py --x 0 --y 0
...
```

and so on. The banner will print a nice banner before you execute the real
function so it is easier to monitor when execution

To create a shell script, simply redirect it into a file such as

```bash
$ python sweep-generator.py sweep.sh
```

Now you can execute it with 

```bash
$ sh sweep.sh | tee result.log
```

The `tee` command will redirect the output to the file result, while still
reporting its progress on the terminal. In case you want to run it without
monitoring or tee is not supported properly you just run it as 


```bash
$ sh sweep.sh >result.log
```

In case you need to monitor the progress for the latter you can use 

```bash
$ tail -f result.log
```

The advantage of this approach is that you can in case of a failure identify
which benchmarks succeeded and exclude them from your next run of `sweep.sh` so
you do not have to redo them. This may be useful if you identify that you ran
out of resources for a parameterized run and it crashed.

#### Integrating timers

The beauty about cloudmesh is that it has built-in timers and if properly used
we can use them even across different invocations of the function f.

we simply have to `fgrep` to the log file to extract the information in the `csv` lines with 

```python
fgrep "#csv" result.log
```

This can then be further post-processed.

Cloudmesh also includes a `cloudmesh.Shell.cm_grep`,
`cloudmesh.common.readfile`, and other useful functions to make the processing
of shell scripts and their output easier.

#### Integration of Jupyter Notebooks

Jupyter notebooks provide a simple mechanism to prototype. However, how do we
now integrate them into a benchmarking suite? Certainly, we can just create the
loop in the notebooks conducting the parameter sweep, but in case of a crash,
this becomes highly unscalable.

So what we have to do is augment a notebook so that we can 

1. pass along the parameters,
2. execute it from the command line.

For this, we use `papermill` that allows us to just do these two tasks. INstall
it with

```python
pip install papermill
```

Then when you open up jupyter-lablab and import our code. Create a new cell. In this 
cell you place all parameters for your run that you like to modify such as

```python
x = 0
y = 0
```

This cell can be augmented with a tag called "parameters". To do this open the 
"cog" and enter in the tag name "parameters". Make sure you save the tag and the notebook.
Now we can use `papermill` to run our notebook with parameters such as 

```
$ mkdir benchmark
$ papermill sweep.ipynb benchmark/sweep-0-0.ipynb --x 0 --y 0 | tee benchmark/result-0-0.log
...
```


Naturally, we can auto-generate this as follows

```python
x_min = 0
x_max = 2
d_x = 1
y_min = 0
y_max = 1
d_y = 1
for x in range(x_min, x_max, dx):
    for y in range(y_min, y_max, dy):
        print (f"cms banner f({x}, {y}; "
               f"papermill sweep.ipynb benchmark/sweep-{x}-{y}.ipynb"
               f"    --x {x} --y {y}"
               f"    | tee benchmark/result-{x}-{y}.log")
```

This will produce a series of commands that we can also redirect into a shell
script and then execute

### Combining the logs

As we have the logs all in the benchmark directory, we can even combine them and 
select the `csv` lines with 

```bash
$ cat benchmark/*.log | fgrep "#csv"
```

Now you can apply further processing such as importing it into pandas or any
other spreadsheet-like tools you like to use for the analysis.












