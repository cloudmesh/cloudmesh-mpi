# Futures

Futures is a module of mpi4py which uses the threads of a processor, or separate processes, to run processes in parallel so that they can communicate with one another.

We can test the mpi4py.futures module by running a Python script that computes a Julia set (data defined from a mathematical function).

> ``` python
> !include ../examples/futures/julia-futures.py
> ```

This script, originally created by Lisandro Dalcin at 
https://mpi4py.readthedocs.io/en/stable/mpi4py.futures.html
has been altered to output a png image

Then, open Git Bash, `cd` to the directory where `julia-futures.py` is located, and then run this command in git bash:

`mpiexec -n 1 python julia-futures.py`

Be sure to change the number after -n to the number of cores in your processor. To find the number of cores in your processor, press the Windows key, type
`This PC`, click `Properties`, and then it should say the number of cores next to processor.

After running the command in Git Bash, it should output a visualization of a Julia data set as a png image.

Furthermore, the numba version of the program can be run instead, which is slightly faster.

> ``` python
> !include ../examples/futures/julia-numba.py
> ```

|         |   No Jit (1280x960)  |  Jit Enabled (1280x960) | No Jit (1920x1440) | Jit Enabled (1920x1440) |
|---------|------------|---------------|-------------|------------|
| 6 Cores | 45.134 s   | 44.402 s      |   68.437 s          |   67.637   |
| 5 Cores | 43.223 s   | 42.825 s      |   68.226 s           |   68.443  |
| 4 Cores | 44.746 s   | 44.552 s      |   73.606 s           |   70.257  |
| 3 Cores | 43.026 s   | 44.521 s      |   68.785 s           |   69.487  |
| 2 Cores | 45.578 s   | 45.714 s      |   67.718 s           |   69.326 |
| 1 Core  | 44.898 s   | 45.800 s      |   68.489 s           |   68.610 |

                
