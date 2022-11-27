#!/usr/bin/env python
from distutils.log import debug
import os
import argparse
import psutil

from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import banner
from cloudmesh.common.dotdict import dotdict


# generates label and logfile for this experiment
def get_label(sort, n, p, c, data):
    return f"log/{sort}-{data.node}-{data.user}-{n}-{p}-{c}.log"


# removes square brackets from string ex: "[mp,seq]" -> "mp,seq"
# Paramter.expand will not work with square brackets for strings
def format_sorts(s):
    if s[0] == '[':
        s = s[1:]
    if s[-1] == ']':
        s = s[:-1]
    return s


username = Shell.run('whoami').strip()
hostname = Shell.run('hostname').strip()

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '--processors',
    default="[4]",
    type=str,
    required=True,
    help="array of number of processors as a string")
parser.add_argument(
    '--cores',
    default="[1]",
    type=str,
    required=True,
    help="number of cores used during sorting")
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
    '--sorts',
    type=str,
    required=True,
    default="[mp]",
    help="sorting functions to be run. can be seq (sequential), mp (multiprocessing), sort (l.sort), or sorted (l = sorted(l))")
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
args = parser.parse_args()

data = dotdict(vars(args))
data.sorts = format_sorts(data.sorts)
sorts = Parameter.expand(data.sorts, sep=',')

for sort in sorts:
    # using sort type to determine number of cores being used
    if sort in ["mp", "mp-mergesort", "multiprocessing_mergesort"]:
        p = psutil.cpu_count(logical=False)
        t = psutil.cpu_count()
        data.cores = data.cores.replace("p", str(p)).replace("t", str(t))
    else:
        data.cores = "[1]"
    # print(data.cores)
    # expand into arrays
    cores = Parameter.expand(data.cores)
    sizes = Parameter.expand(data.sizes, sep=',')
    # processors is always one 
    p = 1

    for c in cores:
        for size in sizes:
            run_cmd = f"python run.py --p={p} --c={c} --size={size} --user={data.user} --node={data.node} --sort={sort}"
            # generate log file that data will be stored in
            # p = 1 since only one processor will be used
            log = get_label(sort, size, 1, c, data)
            run_cmd = run_cmd + f" | tee {log}"

            banner(run_cmd)
            os.system(run_cmd)
