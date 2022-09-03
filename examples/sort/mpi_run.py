#!/usr/bin/env python

import os
import click
from cloudmesh.common.util import banner

# take in user input
@click.command()
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
    help="node name for the stopwatch timer")
@click.option(
    '--sort',
    default="mpi_mergesort",
    help="sorting function to run and analyze")
@click.option(
    '--size',
    default="100",
    help="size of array to be sorted as a comma separated string without spaces: 100,200")
@click.option(
    '--repeat',
    default="10",
    help="repeat the experiment the specified number of times")
@click.option(
    '--id',
    default=0,
    help="specify which merge sort to use")
def run(log, user, node, sort, size, repeat, id):
    """
    :param log: data is storted in log file
    :type log: string
    :param user: user name
    :type user: string
    :param node: node name
    :type node: string
    :return: none
    :rtype: none
    """
    # logfile name - where output will be stored
    log = f"log/{sort}-{node}-{user}-{id}-{size}.log"

    # run experiment.py to generate data from specified sort {sort}
    # data is stored in specified log file {log}
    # default size of array to be sorted is 100

    if os.path.exists(log):
        os.remove(log)
    os.system(f"touch {log}")
    # command to run mpi_experiment.py with given user input
    run_experiment = \
        f'./mpi_experiment.py --log={log} --size={size} --id={id} --user={user} --node={node} --repeat={repeat} --sort={sort} | tee {log}'
    # print command
    banner(run_experiment)
    # run command
    os.system(run_experiment)

if __name__ == '__main__':
    run()
