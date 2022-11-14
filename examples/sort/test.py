#!/usr/bin/env python
from distutils.log import debug
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse
import psutil

from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.dotdict import dotdict

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '--sorts',
    type=str,
    required=True, 
    default="[mp]",
    help="sorting functions to be run. can be seq (sequential), mp (multiprocessing), sort (l.sort), or sorted (l = sorted(l))")
args = parser.parse_args()

data = dotdict(vars(args))
sorts = Parameter.expand(data.sorts, sep=',')

for s in sorts:
    print(s)
    print(type(s))

s = "[100]"
print(s[1:])
print(s[:-1])