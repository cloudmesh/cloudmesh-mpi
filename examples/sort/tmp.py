from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import yn_choice
from cloudmesh.common.util import banner
from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.dotdict import dotdict

import os
import time

data = dotdict()
data.n = 1
data.label = "silly"
for i in range(0, 2):
    StopWatch.start(f"sandra-{i}")
    time.sleep(1.0)
    StopWatch.stop(f"sandra-{i}")
StopWatch.benchmark(tag=str(data))