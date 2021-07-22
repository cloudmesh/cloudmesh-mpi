# Futures

- [ ] Jacques, Identify example to do
- [ ] Convert to png
- [ ] Copy the include statement and add .py to examples folder. examples/julia/julia-futures.py
- [ ] examples/julia/julia-numba.py
- [ ] numba and modin (modin works on dataframes) 
- [ ] @jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
- [ ] cloudmesh stopwatch to compare times with and without numba (jit)
- [ ] if rank = 0 then stopwatch start, and same but with stop at end

Futures is a module of mpi4py which uses the threads of a processor, or separate processes, to run processes in parallel so that they can communicate with one another.

We can test the mpi4py.futures module by running a Python script that computes a Julia set (data defined from a mathematical function).

Credit to Lisandro Dalcin for this script, taken from https://mpi4py.readthedocs.io/en/stable/mpi4py.futures.html

```
from mpi4py.futures import MPIPoolExecutor

x0, x1, w = -2.0, +2.0, 640*2
y0, y1, h = -1.5, +1.5, 480*2
dx = (x1 - x0) / w
dy = (y1 - y0) / h

c = complex(0, 0.65)

def julia(x, y):
    z = complex(x, y)
    n = 255
    while abs(z) < 3 and n > 1:
        z = z**2 + c
        n -= 1
    return n

def julia_line(k):
    line = bytearray(w)
    y = y1 - k * dy
    for j in range(w):
        x = x0 + j * dx
        line[j] = julia(x, y)
    return line

if __name__ == '__main__':

    with MPIPoolExecutor() as executor:
        image = executor.map(julia_line, range(h))
        with open('julia.pgm', 'wb') as f:
            f.write(b'P5 %d %d %d\n' % (w, h, 255))
            for line in image:
                f.write(line)
```

First, copy this code and save it as `julia.py` in a directory you can navigate to via git bash. This can be done with PyCharm.

Then, open Git Bash, `cd` to the directory where `julia.py` is located, and then run this command in git bash:

`mpiexec -n 1 python julia.py`

Be sure to change the number after -n to the number of cores in your processor. To find the number of cores in your processor, press the Windows key, type
`This PC`, click `Properties`, and then it should say the number of cores next to processor.


                
