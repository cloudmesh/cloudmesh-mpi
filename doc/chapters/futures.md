# Futures

- [ ] examples/julia/julia-numba.py
- [ ] numba and modin (modin works on dataframes) 
- [ ] @jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
- [ ] cloudmesh stopwatch to compare times with and without numba (jit)
- [ ] if rank = 0 then stopwatch start, and same but with stop at end

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


                
