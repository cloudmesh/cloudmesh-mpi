#! (penv)
"""

describe what this is

"""
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import writefile
from cloudmesh.common.StopWatch import StopWatch
import random

n = number_of_jobs = 5
maximum_time=10

# SBATCH output /home/pi/{name}-%j-%N.out
# SBATCH output /home/pi/{name}-%j-%N.err

# SBATCH output /nfs/pi/{name}-%j-%N.out
# SBATCH output /nfs/pi/{name}-%j-%N.err

def create_job(name, delay):
    script = \
        f"""
        #!/bin/bash
        #SBATCH -o {name}-%j-%N.out
        #SBATCH -e {name}-%j-%N.err

        hostname
        echo $SLURM_JOB_NAME
        sleep {delay}
        # figure out what the current name is
        
        # cp ${{SLURM_JOB_NAME}}.out /nfs/tmp/
        # cp ${{SLURM_JOB_NAME}}.err /nfs/tmp/
        """.strip()

    print(f'here is name {name}')
    print(f'here is writefile {name}.slurm')
    writefile(f"{name}.slurm", script)


if __name__ == '__main__':
    Shell.run("mkdir -p /nfs/tmp/")
    total = 0.0
    StopWatch.start(f"{n}-jobs")
    for i in range (100):
        name = f"job-{i}"
        t = random.random() * maximum_time
        total = total + t
        create_job(name, t)
        print(f"here is sbatch {name}.slurm")
        result = Shell.run(f"sbatch {name}.slurm")
        print()

    # look ofe 100 and check if all were executed
    # are all output files generated (100)

    # do other stuff

    StopWatch.stop(f"{n}-jobs")
    StopWatch.benchmark()

    print(total)