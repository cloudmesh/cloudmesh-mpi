#!/usr/bin/env python
from sequential.mergesort import mergesort
from util.generate import Generator
from mpi_sort import mpi_sort
from mpi4py import MPI

arr = Generator.generate_random(100)
print(arr)
arr = mpi_sort('<', arr, 4, 1, 'sorted', 'merge')
print(arr)