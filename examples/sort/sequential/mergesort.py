# merge sort
# https://www.educative.io/edpresso/merge-sort-in-python

import os
import click
import sys
import numpy as np
from cloudmesh.common.dotdict import dotdict

config = dotdict()
config.algorithm = sorted

config.user = "gregor"
config.node = "5090X"
config.debug = False
config.benchmark = True
config.filename = sys.argv[0].replace(".py", "")
config.id = 0
# config.merge = "sequential"
n = config.size = 10000
# config.min_array_size = 1

# take in input from user
for arg in sys.argv[1:]:
    if arg.startswith("node="):
        config.node = arg.split("=")[1]
    elif arg.startswith("user="):
        config.user = arg.split("=")[1]
    elif arg.startswith("n="):
        config.size = int(arg.split("=")[1])
    elif arg.startswith("id="):
        config.id = int(arg.split("=")[1])
    elif arg.startswith("alg="):
         config.algorithm = arg.split("=")[1]

def merge_sort(array, p):
    if len(array) > 1:

        r = len(array)//2
        left = array[:r]
        right = array[r:]

        merge_sort(left, p)
        merge_sort(right, p)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
