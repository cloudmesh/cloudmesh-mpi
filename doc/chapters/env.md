# Using Environment Variables to Pass Parameters



#os.environ in Python is a mapping object that represents the user’s environmental variables. 
It returns a dictionary having user’s environmental variable as key and their values as value.

os.environ behaves like a python dictionary, so all the common dictionary operations like get and set can be performed.
We can also modify os.environ but any changes will be effective only for the current process where it was assigned and it will not change the value permanently.


## Example

We demonstrate thsi on ana example.
We developed a programm 
count.py  (URL MISSING) program uses os.environ from the os library
to optionally pass parameters to an mpi program.

> ``` python
> !include ../examples/count/count.py
> ```

If the user changed the value of N, MAX, or FIND in the
terminal using, for example, `export FIND="5"` (shown below)
os.environ.get("FIND") would set the find variable equal
to 5.

> ```
> $ export FIND="5"
> $ mpiexec -n 4 python count.py
> 1 0 [9, 6, 8, 3, 4, 8, 5, 6, 6, 3, 5, 6, 10, 5, 5, 1, 1, 2, 1, 3]
> 3 0 [3, 7, 2, 8, 4, 6, 5, 7, 4, 4, 7, 6, 1, 7, 10, 2, 1, 9, 2, 8]
> 2 0 [10, 8, 10, 8, 7, 2, 2, 7, 4, 3, 3, 7, 10, 8, 1, 5, 1, 4, 6, 5]
> 0 0 [5, 8, 9, 1, 2, 7, 1, 5, 5, 6, 3, 6, 10, 9, 7, 10, 5, 3, 6, 5]
> 0 [0, 0, 0, 0]
> Total number of 5's: 0
> ```

However, if the user does not define any evironment
variables, find will default to 8.

> ```
> $ mpiexec -n 4 python count.py
> 1 0 [5, 5, 2, 6, 6, 3, 5, 3, 3, 2, 3, 9, 7, 1, 3, 7, 1, 7, 1, 3]
> 3 1 [7, 1, 5, 1, 2, 2, 10, 7, 2, 1, 2, 6, 4, 6, 10, 10, 5, 8, 10, 10]
> 2 0 [5, 1, 4, 4, 9, 9, 5, 1, 1, 3, 9, 3, 5, 2, 5, 7, 9, 7, 10, 5]
> 0 1 [6, 6, 5, 6, 4, 10, 3, 5, 5, 2, 5, 2, 7, 6, 7, 8, 5, 7, 6, 4]
> 0 [1, 0, 0, 1]
> Total number of 8's: 2
> ```
