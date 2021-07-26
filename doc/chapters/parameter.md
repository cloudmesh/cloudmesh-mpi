# Parameters

```
$ export N=10
$ echo $N
$ python -i
>>> import os
>>> os.environ["N"]
>>> exit()
$ python a.py
$ sh run.sh
$ sh run.sh | fgrep "csv,processors"
$ python b.py
$ python b.py --n=3
```

- [x] Document the .py files in the parameters folder in examples
- [x] Document click module
- [ ] Add parameter passing section
- [x] you can do !include which should be in the mpi documentation to refer to

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