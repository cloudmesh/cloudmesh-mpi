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
    '--size',
    default="100",
    help="size of array to be sorted as a comma separated string without spaces: 100,200")
@click.option(
    '--repeat',
    default="10",
    help="repeat the experiment the specified number of times")
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

    repeat = int(repeat)
    sizes = size.split(",")
    sizes = [int(x) for x in sizes]
    # run experiment.py to generate data from specified sort {sort}
    # data is stored in specified log file {log}
    # default size of array to be sorted is 100

    if os.path.exists(log):
        os.remove(log)
    os.system(f"touch {log}")
    for size in sizes:
        for i in range(int(repeat)):
            command = \
                f'n={size} node={node} user={user} REPEAT={i} mpiexec -n 4 python night.py | tee -a {log}'
            banner(command)
            os.system(command)

    ## run analysis.py on data generated from experiment.py
    ## currently outputs graph of processes and time
    # run_analysis = f"python ./analysis.py --log={log} --size={size} --sort={sort}"
    # banner(run_analysis)
    # os.system(run_analysis)


if __name__ == '__main__':
    run()
