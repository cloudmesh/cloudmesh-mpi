#!/usr/bin/env python

"""
run with:
    ./run.py --user=[user name] --node=[node name for stopwatch] --sort=[sort algorithm]

    Example:
        ./run.py  --size=10000000 --repeat=1 --user=gregor --node=5950x

"""

import os

import click

from cloudmesh.common.util import banner


@click.command()
@click.option(
    '-p',
    default=False,
    is_flag=True,
    help="# of physical cores only")
@click.option(
    '-t',
    default=True,
    is_flag=True,
    help="logical CPUs: # of physical cores times number of threads on each core")
@click.option(
    '--log',
    default=None)
@click.option(
    '--user',
    default=None,
    help="a user for the stopwatch timer")
@click.option(
    '--node',
    default=None,
    help="a node name for the stopwatch timer")
@click.option(
    '--sort',
    default="multiprocessing_mergesort",
    help="sorting function to run and analyze")
@click.option(
    '--size',
    default="[100]",
    help="size")
@click.option(
    '--repeat',
    default="10",
    help="repeat")
def run(p, t, log, user, node, sort, size, repeat):
    """
    :param p: number of physical cores on computer
    :type p: int
    :param t: number of logical CPUs (# of physical cores x number of threads on each core)
    :type t: int
    :param log: data is storted in log file
    :type log: string
    :param user: user name
    :type user: string
    :param node: node name
    :type node: string
    :param sort: type of sort being run
    :type sort: string
    :return: none
    :rtype: none
    """
    if p:
        n = "p"
    else:
        n = "t"

    if log is None:
        log = f"log/{sort}-{node}-{user}-{size}.log"

    # run experiment.py to generate data from specified sort {sort}
    # data is stored in specified log file {log}
    # default size of array to be sorted is 100

    run_experiment = \
        f'python ./experiment.py --user={user} --node={node} --log={log}' \
        f' --processes="[1-{n}]" --size="{size}" --repeat={repeat} --sort={sort} |tee {log}'
    banner(run_experiment)
    os.system(run_experiment)

    ## run analysis.py on data generated from experiment.py
    ## currently outputs graph of processes and time
    # run_analysis = f"python ./analysis.py --log={log} --size={size} --sort={sort}"
    # banner(run_analysis)
    # os.system(run_analysis)


if __name__ == '__main__':
    run()
