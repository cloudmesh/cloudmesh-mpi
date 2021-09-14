#!/usr/bin/env python
from mpi4py import MPI
import numpy
import time
import sys


icomm = MPI.COMM_WORLD

N = numpy.array(0, dtype='i')
comm.Bcast([N, MPI.INT], root=0)
print(f"N: {N} rank: {rank}")

h = 1.0 / N
s = 0.0
for i in range(rank, N, size):
    x = h * (i + 0.5)
    s += 4.0 / (1.0 + x**2)
PI = numpy.array(s * h, dtype='d')
icomm.Reduce([PI, MPI.DOUBLE], None,
            op=MPI.SUM, root=0)

time.sleep(30)

#time.sleep(60)
icomm.Disconnect()

#MPI.Finalize()
#sys.exit()
#MPI.Unpublish_name()
#MPI.Close_port()
