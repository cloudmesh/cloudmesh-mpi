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

#### l.sort()

- URL to code
- how to run
- what is output

#### sorted(l)

#### Adaptive Merge Sort

### Multiprocessing Merge Sort

### MPI Merge Sort

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