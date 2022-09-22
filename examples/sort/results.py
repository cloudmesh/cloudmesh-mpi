import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from cloudmesh.common.util import banner
from analysis import get_data
from analysis import read_log, read_logs
from analysis import generate_average
from numba import jit, cuda

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

user = "alex"
node = "v100"
sorts = ["mp-mergesort"]
sort = "mp-mergesort"

sizes = [100, 1000, 1e3, 1e4, 1e5, 1e6, 5*1e6, 1e7, 1e8]
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
