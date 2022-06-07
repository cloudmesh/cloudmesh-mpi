#! (penv)
"""

this program must be run in
the manager node's home directory.
it creates 100 jobs to be run
randomly distributed among the
specified nodes, and puts the
output in /nfs/tmp/.

"""
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import writefile
from cloudmesh.common.StopWatch import StopWatch
import random
import textwrap
import os

n = number_of_jobs = 5
maximum_time = 10


# SBATCH output /home/pi/{name}-%j-%N.out
# SBATCH output /home/pi/{name}-%j-%N.err

# SBATCH output /nfs/pi/{name}-%j-%N.out
# SBATCH output /nfs/pi/{name}-%j-%N.err

def create_job(name, delay):
    script = textwrap.dedent(
        f"""
        #!/bin/bash
        #SBATCH -o {name}.out
        #SBATCH -e {name}.err

        hostname
        echo $SLURM_JOB_NAME
        NAME="${{SLURM_JOB_NAME%%.*}}"
        echo $NAME
        sleep {delay}

        cp ${{NAME}}.out /nfs/tmp/
        cp ${{NAME}}.err /nfs/tmp/
        """).strip()

    writefile(f"{name}.slurm", script)


if __name__ == '__main__':
    Shell.run("mkdir -p /nfs/tmp/")
    total = 0.0
    StopWatch.start(f"{n}-jobs")
    for i in range(100):
        name = f"job-{i}"
        t = random.random() * maximum_time
        total = total + t
        create_job(name, t)
        result = Shell.run(f"sbatch {name}.slurm")

    # look ofe 100 and check if all were executed
    # are all output files generated (100)

    # do other stuff

    StopWatch.stop(f"{n}-jobs")
    StopWatch.benchmark()

    print(total)