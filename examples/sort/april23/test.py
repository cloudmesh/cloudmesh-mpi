#!/usr/bin/env python
from sequential.mergesort import mergesort
from util.generate import Generator
from mpi4py import MPI
from mpi_sort_new import mpi_sort
from cloudmesh.common import StopWatch

N = 10000

arr = Generator.generate_random(100)
# print(arr)
arr = mpi_sort('<', arr, 4, 1, 'sorted', 'merge')
# print(arr)