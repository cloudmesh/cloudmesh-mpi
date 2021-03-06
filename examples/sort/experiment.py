#!/usr/bin/env python
import os
import platform

import click
import psutil

from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import yn_choice
from cloudmesh.common.systeminfo import os_is_windows
from generate import Generator


def get_sort_by_name(name="multiprocessing_mergesort"):
    if name in ["mp-mergesort", "multiprocessing_mergesort"]:
        from multiprocessing_mergesort import multiprocessing_mergesort
        return multiprocessing_mergesort
    else:
        return None


def get_label(name, p, n, i, tag=None):
    if tag is None:
        if not os_is_windows:
            tag = os.uname().nodename
        else:
            tag = platform.uname().node
    return f"{tag}_{name}_{p}_{n}_{i}"


username = Shell.run('whoami').strip()
hostname = Shell.run('hostname').strip()


@click.command()
@click.option(
    '--processes',
    default="[1]",
    help='Number of processes as array. [1-2,8,16]')
@click.option(
    '--size',
    default="[100]",
    help='Total size of the array to be sorted as array. [10, 100]')
@click.option(
    '--repeat',
    default=1,
    help='number of times an experiment with processes and size is repeated. 1')
@click.option(
    '--log',
    default="output.log",
    help='The logfile to which the experiments are appended')
@click.option(
    '--clear',
    default=False,
    help='Clears the logfile. Handle with care')
@click.option(
    '--debug',
    default=False,
    help='Switch on some debugging')
@click.option(
    '--sort',
    default="multiprocessing_mergesort",
    help="sorting function")
@click.option(
    '--tag',
    default=None,
    help="a prefix for the stopwatch timer name")
@click.option(
    '--user',
    default=username,
    help="a user for the stopwatch timer")
@click.option(
    '--node',
    default=hostname,
    help="a node name for the stopwatch timer")
def experiment(processes, size, repeat, log, clear, debug, sort, tag, user, node):
    """
    performance experiment.

    :param processes:
    :type processes:
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

    p = psutil.cpu_count(logical=False)
    t = psutil.cpu_count()

    processes = processes.replace("p", str(p)).replace("t", str(t))
    processes = Parameter.expand(processes)
    sizes = Parameter.expand(size)

    processes = [int(number) for number in processes]
    sizes = [int(number) for number in sizes]

    total = len(processes) * len(sizes) * repeat

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
    print(f"Tag:       {tag}")
    print(f"Total:     {total}")

    sort_algorithm = get_sort_by_name(sort)

    last_time = "undefined"
    c = 0
    for p in processes:
        for n in sizes:
            for i in range(repeat):
                c = c + 1
                progress = total - c
                print(f"Experiment {progress:<10}: size={n} processes={p} repeat={i} last_time={last_time}"
                      "                     ",
                      end="\r")
                label = get_label(sort, p, n, i, tag)
                a = Generator().generate_random(n)
                StopWatch.start(label)
                a = sort_algorithm(a, p)
                StopWatch.stop(label)
                last_time = StopWatch.get(label)
                #assert verify("ascending", a)

    StopWatch.benchmark(user=user, node=node)


if __name__ == '__main__':
    log, processes, sizes, repeat, clear, debug = experiment()
