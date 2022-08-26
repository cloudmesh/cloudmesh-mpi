#!/usr/bin/env python

import os
import click
from cloudmesh.common.util import banner

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
    default="0",
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
    log = f"log/{sort}-{node}-{user}-{id}-{size}.log"

    # run experiment.py to generate data from specified sort {sort}
    # data is stored in specified log file {log}
    # default size of array to be sorted is 100

    if os.path.exists(log):
        os.remove(log)
    os.system(f"touch {log}")
    run_experiment = \
        f'./mpi_experiment.py --log={log} --size={size} --id={id} --user={user} --node={node} --repeat={repeat} --sort={sort} | tee {log}'
    banner(run_experiment)
    os.system(run_experiment)

    ## run analysis.py on data generated from experiment.py
    ## currently outputs graph of processes and time
    # run_analysis = f"python ./analysis.py --log={log} --size={size} --sort={sort}"
    # banner(run_analysis)
    # os.system(run_analysis)


if __name__ == '__main__':
    run()
