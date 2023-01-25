import os
import sys
from threading import local
import platform
import numpy as np
import click
from generate import Generator
import jax

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.Shell import Shell
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import yn_choice
from cloudmesh.common.util import banner
from cloudmesh.common.systeminfo import os_is_windows


@click.command()
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
@click.option(
    '--id',
    default=0,
    help="specify which merge sort to use")
def experiment(size, repeat, log, clear, debug, sort, tag, user, node, id):
    if log is None:
        log = f"log/{sort}-{node}-{user}-{id}-{size}.log"


n = 100
a = np.array(Generator().generate_random(n))
print(a)
a = jax.numpy.sort(a)
print(a)
