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
from generate import Generator

# generates label for this experiment
def get_label(name, p, n, i, id, tag=None):
    if tag is None:
        if not os_is_windows:
            tag = os.uname().nodename
        else:
            tag = platform.uname().node
    return f"{tag}_{name}_{p}_{n}_{id}_{i}"

username = Shell.run('whoami').strip()
hostname = Shell.run('hostname').strip()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--processors', 
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
    required=True, 
    help='number of times an experiment with processes and size is repeated')
parser.add_argument(
    '--log',
    type=str, 
    default="output.log", 
    help='the logfile to which the experiments are appended')
parser.add_argument(
    '--clear',
    type=bool,
    default=False,
    help='clears the logfile. handle with care')
parser.add_argument(
    '--debug',
    type=bool,
    default=False,
    help='switch on some debugging')
parser.add_argument(
    '--sort',
    type=str,
    required=True,
    default="multiprocessing_mergesort",
    help="sorting function to be run")
parser.add_argument(
    '--tag',
    default=None,
    help="a prefix for the stopwatch timer name")
parser.add_argument(
    '--user',
    type=str,
    default=username,
    help="username, used in logfile naming")
parser.add_argument(
    '--node',
    type=str,
    default=hostname,
    help="a node name, used in logile naming")
parser.add_argument(
    '--id',
    type=str,
    default=0,
    help="specify which merge sort to use")

def experiment(processes, size, repeat, log, clear, debug, sort, tag, user, node, id):
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

    if clear:
        c = yn_choice("Would you like to clear the file {log} before running the experiements")
        if not c:
            return ""
    if log is None:
        log = f"log/{sort}-{node}-{user}-{id}-{size}.log"

    processes = Parameter.expand(processes)
    sizes = Parameter.expand(size)

    processes = [int(number) for number in processes]
    sizes = [int(number) for number in sizes]

    total = len(processes) * len(sizes) * repeat

    # begin running experiment
    print("Starting experiment")

    #processes = processes.reverse()
    processes.sort(reverse=True)
    print(f"Log:       {log}")
    print(f"Processes: {processes}")
    print(f"Size:      {sizes}")
    print(f"Repeat:    {repeat}")
    print(f"Clear:     {clear}")
    print(f"Debug:     {debug}")
    print(f"Algorithm: {sort}")
    print(f"ID:        {id}")
    print(f"Tag:       {tag}")
    print(f"Total:     {total}")

    last_time = "undefined"
    c = 0
    for p in processes:
        for n in sizes:
            for i in range(repeat):
                c = c + 1
                progress = total - c
                print(f"Experiment {progress:<10}: size={n} processes={p} id={id} repeat={i} last_time={last_time}"
                      "                     ",
                      end="\n")
                label = get_label(sort, p, n, i, id, tag)

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
                    f'mpiexec -n {p} python night.py n={n} node={node} user={user} alg={algorithm} REPEAT={i}'

                # start timer
                StopWatch.start(label)
                # run command
                os.system(command)
                # stop timer
                StopWatch.stop(label)
                last_time = StopWatch.get(label)

    # print out collected information
    StopWatch.benchmark(user=user, node=node)

if __name__ == '__main__':
    log, processes, sizes, repeat, clear, debug = experiment()
