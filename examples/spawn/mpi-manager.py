#!/usr/bin/env python
from mpi4py import MPI
import numpy
import sys
import psutil

comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['mpi-worker.py'],
                           maxprocs=(psutil.cpu_count(logical=False) - 1))

N = numpy.array(100, 'i')
comm.Bcast([N, MPI.INT], root=MPI.ROOT)
PI = numpy.array(0.0, 'd')
comm.Reduce(None, [PI, MPI.DOUBLE],
            op=MPI.SUM, root=MPI.ROOT)
print(PI)

comm.Disconnect()
