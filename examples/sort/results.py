#!/usr/bin/env python
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse
import psutil

from analysis import get_data
from analysis import read_log, read_logs
from analysis import generate_average
from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import yn_choice
from cloudmesh.common.util import banner
from cloudmesh.common.dotdict import dotdict
from generate import Generator

# generates label and logfile for this experiment
def get_label(data):
    return f"{data.sort}-{data.node}-{data.user}-{data.size}-{data.p}-{data.t}-{data.c}"

username = Shell.run('whoami').strip()
hostname = Shell.run('hostname').strip()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--processors', 
    default="[4]",
    type=str, 
    required=False,
    help="array of number of processors as a string")
parser.add_argument(
    '--sizes', 
    default="[100]",
    type=str, 
    required=False, 
    help='sizes of the arrays to be sorted as a string')
parser.add_argument(
    '--repeat',
    default=10,
    type=int, 
    required=False, 
    help='number of times an experiment with processes and size is repeated')
parser.add_argument(
    '--log',
    type=str, 
    required=False, 
    default="output.log", 
    help='the logfile to which the experiments are appended')
parser.add_argument(
    '--clear',
    type=bool,
    required=False, 
    default=False,
    help='clears the logfile. handle with care')
parser.add_argument(
    '--debug',
    type=bool,
    required=False,
    default=False,
    help='switch on some debugging')
parser.add_argument(
    '--sort',
    type=str,
    required=False, 
    default="mp",
    help="sorting function to be run. can be seq (sequential), mp (multiprocessing), or mpi.")
parser.add_argument(
    '--tag',
    required=False, 
    default=None,
    help="a prefix for the stopwatch timer name")
parser.add_argument(
    '--user',
    type=str,
    required=False, 
    default=username,
    help="username, used in logfile naming")
parser.add_argument(
    '--node',
    type=str,
    required=False, 
    default=hostname,
    help="a node name, used in logile naming")
parser.add_argument(
    '--t',
    type=int,
    required=False, 
    default=None,
    help="number of threads per core")
parser.add_argument(
    '--c',
    type=int,
    required=False, 
    default=None,
    help="number of cores")
parser.add_argument(
    '--id',
    type=str,
    required=False, 
    default=0,
    help="specify which merge sort to use")
args = parser.parse_args()

data = dotdict(vars(args))
'''
Usage:
docopt.py seq [options] [operation] [seq-option]
docopt.py mp [options] [operation] [mp-option]
docopt.py mpi [options] [operation] [mpi-option]
operation:
   --area=<bool>       Calculate the area if the argument==True
   --perimeter=<bool>  Calculate the perimeter if the argument==True
seq-option:
   --edge=<float>      Edge of the square. [default: 2]
mp-option:
   --height=<float>    Height of the rectangle 
   --width=<float>     Width of the rectangle 
mpi-option:
   --height=<float>    Height of the rectangle 
   --width=<float>     Width of the rectangle 
'''

if sort in ["mp-mergesort", "multiprocessing_mergesort"]:
    p = psutil.cpu_count(logical=False)
    t = psutil.cpu_count()
else:
    p = 1
    t = 1
processors = Parameter.expand(data.processors)
sizes = Parameter.expand(data.sizes)

# this will take a long time. 
# also if you don't want to use all your processors then use different commands. 
for sort in sorts:
    for size in sizes:
        run_cmd = f"./run.py --user={user} --node={node} --size={size} --sort={sort}"

        if "mpi" in sort:
            run_cmd = f"./mpi_run.py --user={user} --node={node} --sort={sort}--size={size} --id={0}"
        else:
            run_cmd = f"./run.py --user={user} --node={node} --size={size} --sort={sort}"
        banner(run_cmd)
        os.system(run_cmd)


# files = ["alex"]
# sorts = ["seq-merge", "mp-mergesort"]

