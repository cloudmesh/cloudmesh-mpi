from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import yn_choice
from cloudmesh.common.util import banner
from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.dotdict import dotdict

import os
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--processors',
    default=4,
    type=int,
    required=False,
    help="number of processors as an integer")
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
args = parser.parse_args()

data = dotdict(vars(args))

# data = dotdict()
# data.n = 1
# data.label = "silly"
for i in range(0, 2):
    StopWatch.start(f"sandra-{i}")
    time.sleep(1.0)
    StopWatch.stop(f"sandra-{i}")
StopWatch.benchmark(tag=str(data))
