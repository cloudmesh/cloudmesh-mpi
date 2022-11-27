#!/usr/bin/env python
import os
import platform
import argparse
import numpy as np

from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.dotdict import dotdict
from sequential.mergesort import merge_sort
from multiprocessing_mergesort import multiprocessing_mergesort

# generates label and logfile for this experiment
def get_label(data, i):
    return f"{data.sort}-{data.node}-{data.user}-{data.size}-{data.p}-{data.c}-{i}"

# filters unneccessary data out of the arguments parsed from command line
# to be printed out from the stopwatch
def data_to_benchmark(data):
    ans = data
    rm = ['log', 'clear', 'debug', 'tag', 'id']
    for key in rm:
        if key in ans:
            ans.pop(key)
    
    for key in data:
        if data[key] == None:
            data[key] = "None"
    return ans

# maps between common nicknames of sorts and the sort type accepted by program
def get_sort_by_name(name="multiprocessing_mergesort"):
    if name in ["mp", "mp-merge", "mp-mergesort", "multiprocessing_mergesort"]:
        # print("MP SORT")
        return multiprocessing_mergesort
    elif name in ["seq", "seq-mergesort", "seq-merge", "sequential_merge", "sequential_mergesort"]:
        # print("MERGE SORT")
        return merge_sort

def get_np_sort_kind(name):
    if "quick" in name:
        return "quicksort"
    elif "merge" in name:
        return "mergesort"
    elif "heap" in name:
        return "heapsort"
    elif "stable" in name:
        return "stable"
    else:
        return "INVALID SORT TYPE"
    
username = Shell.run('whoami').strip()
hostname = Shell.run('hostname').strip()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--p', 
    default=4,
    type=int, 
    required=True,
    help="number of processes as an integer")
parser.add_argument(
    '--c',
    type=int,
    required=True, 
    default=None,
    help="number of cores")
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
    help="a node name, used in logfile naming")
args = parser.parse_args()

data = dotdict(vars(args))
data.debug = False

def experiment(p, c, size, repeat, log, clear, debug, sort, tag, user, node):
    """
    performance experiment.

    :param p: number of processes to use. this is single processor run file, so will always be 1.
    :type p: int
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
    repeat = 5 # hardcoding to make runs faster
    total = repeat

    # map from alias to sort
    if "np" in sort:
        sort_kind = get_np_sort_kind(sort)
    sort_algorithm = get_sort_by_name(sort)
    if debug:
        print(sort_algorithm)
    
    # sequential merge sort only runs on one process
    if sort_algorithm != multiprocessing_mergesort:
        data.p = 1
        p = 1

    # begin running experiment
    print("Starting experiment")

    print(f"Processes: {p}")
    print(f"Cores:     {c}")
    print(f"SORT:      {sort}")
    print(f"Size:      {size}")
    print(f"Repeat:    {repeat}")
    print(f"Debug:     {debug}")
    print(f"Algorithm: {sort}")
    print(f"Tag:       {tag}")
    print(f"Total:     {total}")

    last_time = "undefined"
    count = 0
    n = size
    for i in range(repeat):
        count = count + 1
        progress = total - count
        print(f"Experiment {progress:<5}: sort={sort} size={n} processes={p} cores={c} repeat={i} last_time={last_time}"
                "                     ",
                end="\n")
        label = get_label(data, i)

        # generate unsorted array
        a = np.random.randint(n, size=n)
        if data.debug:
            print(a)
        list_a = a.tolist()

        # start timer
        StopWatch.start(label)
        # run command
        if "np" in sort:
            if data.debug:
                print(f"SORT KIND={sort_kind}")
                print(f"ARRAY TYPE={type(a)}")
                print(a)
            a = np.sort(a, kind=sort_kind)
            if data.debug:
                print(a)
        elif sort == 'sort':
            if data.debug:
                print(f"SORT KIND={sort}")
                print(f"ARRAY TYPE={type(list_a)}")
                print(list_a)
            list_a.sort()
            if data.debug:
                print(list_a)
        elif sort == 'sorted':
            if data.debug:
                print(f"SORT KIND={sort}")
                print(f"ARRAY TYPE={type(list_a)}")
                print(list_a)
            list_a = sorted(list_a)
            if data.debug:
                print(list_a)
        else:
            list_a = sort_algorithm(list_a, c)
        # stop timer
        StopWatch.stop(label)
        last_time = StopWatch.get(label)
        if data.debug:
            print(a)

    # print out collected information
    benchmark_data = data_to_benchmark(data)
    StopWatch.benchmark(tag=str(benchmark_data))
    
if __name__ == '__main__':
    experiment(args.p, args.c, args.size, args.repeat, args.log, args.clear, args.debug, args.sort, args.tag, args.user, args.node)
