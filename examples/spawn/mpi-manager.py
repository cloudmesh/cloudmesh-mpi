#!/usr/bin/env python
from mpi4py import MPI
import mpi4py
import numpy
import sys
import time
from pprint import pprint
print("Hello")

print ("argv", sys.argv)

#print ("ENV", dict(mpi4py.MPI.INFO_ENV))
import os

#pprint (dict(os.environ))

comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['mpi-worker.py'],
                           maxprocs=2)
rank = comm.Get_rank()
print(f"b and rank: {rank}")

N = numpy.array(100, 'i')
comm.Bcast([N, MPI.INT], root=MPI.ROOT)
#print(f"ROOT: {MPI.ROOT}")
print('c')
PI = numpy.array(0.0, 'd')

print('d')
comm.Reduce(None, [PI, MPI.DOUBLE],
            op=MPI.SUM, root=MPI.ROOT)
print(PI)

comm.Disconnect()
