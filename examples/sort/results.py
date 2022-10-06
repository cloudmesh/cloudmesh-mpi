import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from cloudmesh.common.util import banner
from analysis import get_data
from analysis import read_log, read_logs
from analysis import generate_average

user = "alex"
node = "aim"
#sorts = ["seq-mergesort", "mp-mergesort"]
sorts = ["mp-mergesort"]

#sizes = [1000, 10000]
sizes = [1e5, 1e6]
sizes = [int(size) for size in sizes]

# this will take a long time. 
# also if you don't want to use all your processors then use different commands. 
for sort in sorts:
    for size in sizes:
        run_cmd = f"./run.py --user={user} --node={node} --size={size} --sort={sort}"

        if "mpi" in sort:
            run_cmd = f"./mpi_run.py --user={user} --node={node} --sort={sort}--size={size} --id={0}"
        else:
            run_cmd = f"./run.py --user={user} --node={node} --size={size} --sort={sort}"
        banner(run_cmd)
        os.system(run_cmd)


# files = ["alex"]
# sorts = ["seq-merge", "mp-mergesort"]

