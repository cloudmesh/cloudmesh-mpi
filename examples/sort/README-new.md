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

### Sequential Merge Sort

The sequential merge sort algorithm is located [here](https://github.com/cloudmesh/cloudmesh-mpi/blob/main/examples/sort/sequential/mergesort.py).

#### l.sort()


- how to run
- what is output

#### sorted(l)

#### Adaptive Merge Sort

### Multiprocessing Merge Sort

Run using the command

  ```bash
  python run.py  --p=8 --size=80 --user=alex --node=v100 --sort=mp --debug=true
  ```

### MPI Merge Sort

Run using the command

  ```bash 
  python mpi_results.py --p={p} --size={n} --user={user} --node={node} --sort=mpi-mergesort 
  ```

  ```bash
  All of the options below are REQUIRED to run the command. 

  p = number of processors to sort on
  n = size of array to sort
  user = convenient unique name (not username on host) that identifies user
  node = name of host machine on which benchmark is executed
  sort = name by which to identify and print sort (should always just use mpi-mergesort)

  Below are some additional options that are not required. 

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

This generates timer output for the specific conditions input by the user. Note that this does not print any output to the log file. This program is run by results.py. 

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
