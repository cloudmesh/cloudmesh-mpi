#!/usr/bin/env python
from distutils.log import debug
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
def get_label(n, p, data):
    return f"log/{data.sort}-{data.node}-{data.user}-{n}-{p}-{data.t}-{data.c}"

username = Shell.run('whoami').strip()
hostname = Shell.run('hostname').strip()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--processes', 
    default="[4]",
    type=str, 
    required=True,
    help="array of number of processes as a string")
parser.add_argument(
    '--sizes', 
    default="[100]",
    type=str, 
    required=True, 
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
    required=True, 
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
    required=True, 
    default=username,
    help="username, used in logfile naming")
parser.add_argument(
    '--node',
    type=str,
    required=True, 
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

if data.sort in ["mp", "mp-mergesort", "multiprocessing_mergesort"]:
    p = psutil.cpu_count(logical=False)
    t = psutil.cpu_count()
    data.processes = data.processes.replace("p", str(p)).replace("t", str(t))

processes = Parameter.expand(data.processes)
sizes = Parameter.expand(data.sizes, sep=',')

# this will take a long time. 
# also if you don't want to use all your processors then use different commands. 
for p in processes:
    for size in sizes:
        run_cmd = f"./run.py --user={data.user} --node={data.node} --size={size} --sort={data.sort}"

        if "mpi" in data.sort:
            run_cmd = f"python mpi_run.py  --p={p} --size={size} --user={data.user} --node={data.node} --sort=mpi-mergesort --debug={data.debug} --id=0"
        else:
            run_cmd = f"python run.py --p={p} --size={size} --user={data.user} --node={data.node} --sort=mpi-mergesort --debug={data.debug}"

        if data.t != None:
            run_cmd = run_cmd + "--t={data.t}"
        if data.c != None:
            run_cmd = run_cmd + "--c={data.c}"
        
        # generate log file that data will be stored in
        log = get_label(size, p, data)
        run_cmd = run_cmd + f"| tee {log}"

        banner(run_cmd)
        os.system(run_cmd)


# files = ["alex"]
# sorts = ["seq-merge", "mp-mergesort"]

