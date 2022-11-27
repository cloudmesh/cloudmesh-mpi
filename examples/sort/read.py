from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import yn_choice
from cloudmesh.common.util import banner
from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.util import readfile

import os
import time
import json

content = readfile("a.log")
result = []
lines = Shell.find_lines_with(content, "# csv")[1:]
for line in lines:
    line = line.replace("'", '"')
    data = "{" + line.split("{")[1].split("},")[0] + "}"
    data = dotdict(json.loads(data))
    line = line.split(",", 6)
    i = line[1].split("-")[1]
    t = line[3]

    data.t = t
    data.i = i
    result.append(dict(data))
print(json.dumps(result, indent=2))
