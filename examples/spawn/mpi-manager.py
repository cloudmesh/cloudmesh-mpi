#!/usr/bin/env python
from mpi4py import MPI
import mpi4py
import numpy
import sys
import time
from pprint import pprint
from cloudmesh.common.util import banner

comm = MPI.COMM_WORLD
size = comm.Get_size()
name = comm.Get_processor_name()

banner(f"MPI Spawn example {name} {size}")

icomm = MPI.COMM_SELF.Spawn(
    sys.executable,
    args=['mpi-worker.py'],
    maxprocs=size)

rank = icomm.Get_rank()
print(f"rank of {name}: {rank} of {size}")

N = numpy.array(100, 'i')
icomm.Bcast([N, MPI.INT], root=MPI.ROOT)
#print(f"ROOT: {MPI.ROOT}")
print('c')
PI = numpy.array(0.0, 'd')

print('d')
icomm.Reduce(None, [PI, MPI.DOUBLE],
            op=MPI.SUM, root=MPI.ROOT)
print(PI)

time.sleep(30)
icomm.Disconnect()
