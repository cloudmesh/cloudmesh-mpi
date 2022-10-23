# Benchmarking Sorting Algorithms

## Installation

## Log File Formatting

- how we augment source code?

  ```bash
  data = dotdict()
  data.n = size of array
  data.p = number of processors
  data.t = number of threads
  data.c = number of cores
  data.algorithm = "name of algorithm"
  data.host = "name of host machine on which benchmark is executed"
  data.user = "convenient unique name (not username on host) that identifies user (pseudonym for user)"
  data.i = i-th experiment with same parameters
  data.label = "label printed for figures" # label = "rtx3090-amd5095", "macpro2019-i7"
  # do not reveal real usernames on host
  # and any other parameter that may be used
  Stopwatch.benchmark(..., tag=str(data), ...)
  ```

- show how log files are formatted
    - give example of formatted log file
    - name of logfile is ...
      f"{data.algorithm}-{data.host}-{data.user}-{data.n}-{data.p}-{data.t}-{data.c}-{data.i}.log"
    - reasoning for - vs _
- how str(data) looks
  ```bash
  {
      "algorithm": ...,
  }
  ```
  identify where tag is in that line, read in tag as .json object
  will return a dict that can be used for identification purposes
  line = line.split("tag=").split(",",1)[0]
  data = json.loads(line)

## Algorithms

All of the merge sorts should be called and run using **results.py**. 

Note that run.py is used to run both the sequential and the multiprocessing merge sort. This is because both of the sorts can be called in the same way. However, MPI merge sort must be called differently, which is why it has a different run program named mpi_run.py. The run programs generate stopwatch output. However, they do not print to log files, and if run individually, will output to the terminal.  
 
Run results.py using the following command:
```bash
python results.py --processes="[processes]" --sizes="[sizes]"  --sort={sort} --user={user} --node={node}
```

There are five required parameters, which are *processes*, *sizes*, *sort*, *user*, and *node*. 

The *processes* parameter will be described separately for each of the three merge sorts. Below are descriptions of the remaining four required parameters. 

*sizes* is an array of the sizes of the arrays to be sorted. There must be no spaces between the entries of the array, only commas. 
  ```bash
  --sizes=[500,1000]
  ```
This will run the experiment specified by the other parameters on two arrays: one of size 500, and the other of size 1000. Note that if run using the default zsh shell, the entire array must be in string format, since zsh uses square brackets for a predetermined purpose. 
  ```bash
  --sizes="[500,1000]"
  ```
When using other shells, either option (string or not string) will be acceptable. 

*sort* is the specific sort that is to be run. There are three options: sequential merge sort, multiprocessing merge sort, and MPI merge sort. 

Note that to keep the names of the log files uniform, one should only use the following three inputs for the name of the sort function to run:

To run the sequential merge sort, use
  ```bash
  --sort=seq 
  ```

  To run the multiprocessing merge sort, use
  ```bash
  --sort=mp
  ```

  To run the MPI merge sort, use
  ```bash
  --sort=mpi
  ```

*user* is a username used to differentiate different users of this program.

*node* is the host machine upon which this benchmark is run. 

Below are some additional options that are not required. All of these options are available when running any of the three sorts. 
  ```bash
  --repeat={repeat}
  repeat = number of times this experiment will be repeated, with all required options kept constant
  --debug={debug}
  debug = a boolean that defaults to False. when True, this will turn on extra text output to help with debugging
  --tag={tag}
  tag = a string for extra information you might want to include
  --t={t}
  t = number of threads per core
  --c={c}
  c = number of cores
  ```


### Sequential Merge Sort

The sequential merge sort algorithm is located [here](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/sequential/mergesort.py).

Run this using

  ```bash
  python results.py --processes="[processes]" --sizes="[sizes]" --sort=seq --user={user}--node={node}
  ```

This will print the output to logfiles of the format
  ```bash
  seq-{node}-{user}-{size}-{p}-{t}-{c}.log
  ```
for each *size* in *sizes* and each *p* in *processes*. 

Since the sequential merge sort uses only one process to run, *processes* should be input as just

  ```bash
  --processes="[1]"
  ```

However, even if *processes* is incorrectly input, the program will automatically change it to the correct input. 

If you would like to run this using **run.py**, which is the program that runs within results.py, it can be run using

  ```bash
  python run.py --p={p} --size={n} --sort=seq --user={user}--node={node}
  ```
where p is 1 (only one process used) and n is the size of the array to be sorted. This will not print to a log file, rather, it will print directly to the terminal. All optional parameters available in results.py are also available here. 

### Multiprocessing Merge Sort

The multiprocessing merge sort algorithm is located [here](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/multiprocessing_mergesort.py).

Run this using 

  ```bash
  python results.py --processes="[1-p]" --sizes="[sizes]" --sort=mp --user={user} --node={node}
  ```

This will print the output to logfiles of the format
  ```bash
  mp-{node}-{user}-{size}-{p}-{t}-{c}.log
  ```
for each *size* in *sizes* and each *p* in *processes*. 

*processes* can be input in two different ways here. If you would like to run each experiment using every possible number of processes, you can use the range format:
  ```bash
  --processes=[1-p]
  ```
However, if you'd like to run using a specific combination of processes, you can specify using the array format, with an array of numbers separated only by commas, with no spaces in between. 
  ```bash
  --processes=[1,2,5]
  ```
If running inside zsh, the entire array must be enclosed within quotation marks. 

If you would like to run this using **run.py**, which is the program that runs within results.py, it can be run using

  ```bash
  python run.py --p={p} --size={n} --sort=mp --user={user}--node={node}
  ```
where p is the number of processes to use, and n is the size of the array to sort. This will not print to a log file, rather, it will print directly to the terminal. All optional parameters available in results.py are also available here. 

### MPI Merge Sort

The MPI merge sort algorithm is located [here](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/night.py). 

Run this using 

  ```bash
  python results.py --processes="[processes]" --sizes="[sizes]" --sort=mpi --user={user} --node={node}
  ```

This will print the output to logfiles of the format
  ```bash
  mpi-{node}-{user}-{size}-{p}-{t}-{c}.log
  ```
for each *size* in *sizes* and each *p* in *processes*.

*processes* must be input as an array of numbers separated only by commas, with no spaces in between. 
  ```bash
  --processes=[4,8]
  ```
IMPORTANT: every single one of the numbers in *sizes* must be divisible by every single one of the the numbers in *processes*. This is because the MPI merge sort must divide each of the arrays into equal subarrays to send them to each processor to be sorted. This is also why the range format is not available for MPI merge sort. 

If running using zsh, the array must be enclosed within quotation marks. 

If you would like to run this using **mpi_run.py**, which is the program that runs within results.py, it can be run using

  ```bash
  python mpi_run.py  --p={p} --size={n} --sort=mpi-mergesort --user={user} --node={node}
  ```
where p is the number of processors to use, and n is the size of the array to sort. This will not print to a log file, rather, it will print directly to the terminal. All optional parameters available in results.py are also available here. 

##  Analysis

In analysis, we can concatenate any arbitrary logfile and use Jupyter notebooks to conduct the analysis and create performance graphs. 

### Data Selection

- variable n with specified value
- list of experiments

### Speedup

- define speedup
- as n increases
- add examples 
    - where to modify code

### Efficiency

...
