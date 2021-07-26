# Parameters

# Passing Parameters into Git Bash

First create a run.sh shell file with the following contents
```python
N=1; environment-parameter.py
N=2; environment-parameter.py
```

environment-parameter.py and click-parameter.py can be retrieved from examples/parameters.
They must be in the same directory as the previously created run.sh file, and you must cd
(change directory) into this directory in Git Bash.
Input the following commands into Git Bash

```
# This command creates an environment variable called N
$ export N=10
# This command prints the environment variable called N
$ echo $N
# This command launches a Python environment
$ python -i
>>> import os
>>> os.environ["N"]
>>> exit()
$ python environment-parameter.py
$ sh run.sh
$ sh run.sh | fgrep "csv,processors"
$ python click-parameter.py
$ python click-parameter.py --n=3
```

# click-parameter.py

``` python
!include ../examples/parameters/click-parameter.py
```

This Python program sets a variable n (default is 1) and runs a cloudmesh StopWatch
based on the value of the variable n. If n is set to 1, the program waits for a
period of time (0.1 times n), prints the value of n, and then outputs the cloudmesh
benchmark for a number of processors. If n is set to 1, cloudmesh benchmark will only
output 1 processor and the period of time the program waited.

This is meant to be a beginner's basic exploration into the click module.

# environment-parameter.py

``` python
!include ../examples/parameters/environment-parameter.py
```

This Python program does not set a variable N on its own. It refers to os.environ
which should have previously set N as shown in the beginning of this document's
git bash log. The program does the same procedures as the
previous program once N is set and passed from os.environ.
