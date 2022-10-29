#!/usr/bin/env python
from pprint import pprint

import matplotlib.pyplot as plt
import json

from cloudmesh.common.Shell import Shell
from cloudmesh.common.parameter import Parameter
from analysis import read_log

log = "log/mp-v100-alex-100-10-None-None.log"
print(read_log(log))