#!/usr/bin/env python

#
# run with
#
#  ./run.py --log="log/gregor.log" --user=gregor --node=5950x
#

import click
import os
from cloudmesh.common.util import banner


@click.command()
@click.option('-p', default=False, is_flag=True)
@click.option('-t', default=True, is_flag=True)
@click.option('--log', default="output.log")
@click.option('--user', default=None, help="a user for the stopwatch timer")
@click.option('--node', default=None, help="a node name for the stopwatch timer")
def run(p, t, log, user, node):
    if p:
        n = "p"
    else:
        n = "t"

    command = f'python ./experiment.py --user={user} --node={node} --log={log}' \
              f' --processes="[1-{n}]" --size="[100]" --repeat=10 |tee {log}'
    banner(command)
    os.system(command)

    os.system(f"python ./analysis.py --log={log}")

    # | fgrep "# csv" | tee output.log

    # python graph_efficiency.py
    # python graph_speedup.py
    # python graph_proc.py

    # python multiprocessing_mergesort.py "[8]" "[100,1000,10000]" 10 | fgrep "# csv" | tee output-num.log

    # python graph_size.py


if __name__ == '__main__':
    run()
