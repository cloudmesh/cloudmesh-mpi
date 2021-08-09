# Monte Carlo to Recreate the Number Pi

Monte Carlo is a programming term that relies on randomness to generate an intended numerical
result. Python can generate random points within the boundaries of a square; the points that
fall within a circle inside the square can be used to estimate the value of pi to several 
decimal points. 

Recall that pi is a circle's circumference divided by its diameter.

The following program can be used to estimate pi (credit to Cornell University for this
program, retrieved from https://cvw.cac.cornell.edu/python/exercise ):

> ``` python
> !include ../examples/monte-carlo/parallel_pi.py
> ```

The parallel_pi program outputs the sample size of points used in the generation, then
the estimation of pi, and finally the standard deviation of the estimates used for the
sample size.

The program can be accelerated by using a larger MPI size (the default is 1).
To use a larger MPI size, ensure that your terminal is in the same directory
as the parallel_pi.py program. Then, execute the command

`$ mpiexec -n 2 python parallel_pi.py`

The number after `-n` can be as many cores as you have in your processor. For example,
the command will run the program with two cores, ideal for a dual-core CPU. Upon running
this program, it will generate visualizations of the pi value over time and how it slowly
becomes more exact to 3.14159, as well as the number of "darts" (points in the square)
alongside standard deviation.

The following benchmark times were generated using a Ryzen 5 3600 CPU with 16 GB RAM
on a Windows 10 computer.

|         | parallel_pi.py execution time   |
|---------|---------------------------------|
| 6 Cores | 237.873 s                       |
| 5 Cores | 257.720 s                        |
| 4 Cores | 326.811 s                        |
| 3 Cores | 383.343 s                        |
| 2 Cores | 545.500 s                        |
| 1 Core  | 1075.68 s                        |

