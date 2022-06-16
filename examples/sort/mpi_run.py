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
    help="a node name for the stopwatch timer")
@click.option(
    '--size',
    default="100",
    help="size of array to be sorted")
@click.option(
    '--repeat',
    default="10",
    help="repeat sorting how many times")
def run(log, user, node, size, repeat):
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

    if log is None:
        log = f"log/{node}-{user}-{size}.log"

    # run experiment.py to generate data from specified sort {sort}
    # data is stored in specified log file {log}
    # default size of array to be sorted is 100

    run_sort = \
        f'SIZE={size} mpiexec -n 4 python night.py | tee {log}'
    banner(run_sort)
    os.system(run_sort)

    run_sort = \
        f'SIZE={size} mpiexec -n 4 python night.py | tee -a {log}'
    for i in range(int(repeat) - 1):
            banner(run_sort)
            os.system(run_sort)

    ## run analysis.py on data generated from experiment.py
    ## currently outputs graph of processes and time
    # run_analysis = f"python ./analysis.py --log={log} --size={size} --sort={sort}"
    # banner(run_analysis)
    # os.system(run_analysis)


if __name__ == '__main__':
    run()
