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
from sequential.mergesort import merge_sort
from generate import Generator
from multiprocessing_mergesort import multiprocessing_mergesort

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

# maps between common nicknames of sorts and the sort type accepted by program
def get_sort_by_name(name="multiprocessing_mergesort"):
    if name in ["mp", "mp-merge", "mp-mergesort", "multiprocessing_mergesort"]:
        # print("MP SORT")
        return multiprocessing_mergesort
    elif name in ["seq", "seq-mergesort", "seq-merge", "sequential_merge", "sequential_mergesort"]:
        # print("MERGE SORT")
        return merge_sort
    else:
        return None

username = Shell.run('whoami').strip()
hostname = Shell.run('hostname').strip()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--p', 
    default=4,
    type=int, 
    required=False,
    help="number of processes as an integer")
parser.add_argument(
    '--size', 
    type=int, 
    required=False, 
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
    required=False, 
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
    required=False, 
    default=username,
    help="username, used in logfile naming")
parser.add_argument(
    '--node',
    type=str,
    required=False, 
    default=hostname,
    help="a node name, used in logfile naming")
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

    # map from alias to sort
    sort_algorithm = get_sort_by_name(sort)
    
    if sort_algorithm == merge_sort:
        data.p = 1

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
        if data.debug:
            print(a)

        # start timer
        StopWatch.start(label)
        # run command
        a = sort_algorithm(a, p)
        # stop timer
        StopWatch.stop(label)
        last_time = StopWatch.get(label)
        if data.debug:
            print(a)

    # print out collected information
    benchmark_data = data_to_benchmark(data)
    StopWatch.benchmark(tag=str(benchmark_data))
    
if __name__ == '__main__':
    experiment(args.p, args.size, args.repeat, args.log, args.clear, args.debug, args.sort, args.tag, args.user, args.node, args.t, args.c, args.id)
