#!/usr/bin/env python
import os
import platform
import argparse
import psutil

from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import yn_choice
from cloudmesh.common.util import banner
from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.dotdict import dotdict
from generate import Generator

# generates label and logfile for this experiment
def get_label(data, i):
    return f"{data.sort}-{data.node}-{data.user}-{data.size}-{data.p}-{data.t}-{data.c}-{i}"
# filters unneccessary data out of the arguments parsed from command line
# to be printed out from the stopwatch
def data_to_benchmark(data):
    ans = data
    rm = ['log', 'clear', 'debug', 'tag', 'id']
    for key in rm:
        if key in ans:
            ans.pop(key)
    return ans

username = Shell.run('whoami').strip()
hostname = Shell.run('hostname').strip()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--p', 
    default=4,
    type=int, 
    required=True,
    help="number of processors as an integer")
parser.add_argument(
    '--size', 
    type=int, 
    required=True, 
    help='total size of the array to be sorted as an integer')
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
    default="mpi",
    help="sorting function to be run")
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
    
def experiment(p, size, repeat, log, clear, debug, sort, tag, user, node, t, c, id):
    """
    performance experiment.

    :param processes: number of processes to use
    :type processes: hardcoded
    :param size: 
    :type size:
    :param repeat:
    :type repeat:
    :param log:
    :type log:
    :param clear:
    :type clear:
    :param debug:
    :type debug:
    :param sort:
    :type sort:
    :param tag:
    :type tag:
    :param user:
    :type user:
    :param node:
    :type node:
    :return:
    :rtype:
    """

    if log is None:
        log = f"log/{sort}-{node}-{user}-{id}-{size}-{p}-{t}-{c}.log"

    total = repeat

    # begin running experiment
    print("Starting experiment")

    print(f"Log:       {log}")
    print(f"Processes: {p}")
    print(f"Size:      {size}")
    print(f"Repeat:    {repeat}")
    print(f"Clear:     {clear}")
    print(f"Debug:     {debug}")
    print(f"Algorithm: {sort}")
    print(f"ID:        {id}")
    print(f"Tag:       {tag}")
    print(f"Total:     {total}")

    last_time = "undefined"
    c = 0
    n = size
    for i in range(repeat):
        c = c + 1
        progress = total - c
        print(f"Experiment {progress:<10}: size={n} processes={p} id={id} repeat={i} last_time={last_time}"
                "                     ",
                end="\n")
        label = get_label(data, i)

        # generate unsorted array
        a = Generator().generate_random(n)

        # map from id number to sub sort type
        algorithm = "sequential_merge_fast"
        if id == 0:
            algorithm = "sequential_merge_fast"
        elif id == 1:
            algorithm = "sequential_merge_python"
        elif id == 2:
            algorithm = "adaptive_merge"

        # terminal command to run sort program
        command = \
            f'mpirun -n {p} python night.py n={n} log={log} clear={clear} debug={debug} sort={sort} user={user} node={node} id={id} t={t} c={c} REPEAT={i}'

        # start timer
        StopWatch.start(label)
        # run command
        os.system(command)
        # stop timer
        StopWatch.stop(label)
        last_time = StopWatch.get(label)

    # print out collected information
    benchmark_data = data_to_benchmark(data)
    StopWatch.benchmark(tag=str(benchmark_data))

if __name__ == '__main__':
    experiment(args.p, args.size, args.repeat, args.log, args.clear, args.debug, args.sort, args.tag, args.user, args.node, args.t, args.c, args.id)
