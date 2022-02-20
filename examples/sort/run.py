#!/usr/bin/env python
import os

import click

from cloudmesh.common.util import banner


@click.command()
@click.option('-p', default=False, is_flag=True)
@click.option('-t', default=True, is_flag=True)
def run(p, t):
    if p:
        n = "p"
    else:
        n = "t"

    command = f'python ./experiment.py --processes="[1-{n}]" --size="[100]" --repeat=10 | tee output.log'
    banner(command)
    os.system(command)

    os.system("python ./analysis.py")

    # | fgrep "# csv" | tee output.log

    # python graph_efficiency.py
    # python graph_speedup.py
    # python graph_proc.py

    # python multiprocessing_mergesort.py "[8]" "[100,1000,10000]" 10 | fgrep "# csv" | tee output-num.log

    # python graph_size.py


if __name__ == '__main__':
    run()
