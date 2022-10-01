import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from cloudmesh.common.util import banner
from analysis import get_data
from analysis import read_log, read_logs
from analysis import generate_average

user = "alex"
node = "v100"
sorts = ["seq-mergesort", "mp-mergesort"]

sizes = [1000, 10000]
sizes = [int(size) for size in sizes]

# this will take a long time. 
# also if you don't want to use all your processors then use different commands. 
for sort in sorts:
    for size in sizes:
        run_cmd = f"./run.py --user={user} --node={node} --size={size} --sort={sort}"
        banner(run_cmd)
        os.system(run_cmd)


# files = ["alex"]
# sorts = ["seq-merge", "mp-mergesort"]

