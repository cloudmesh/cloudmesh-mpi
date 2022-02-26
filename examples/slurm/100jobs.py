#! (penv)
"""

describe what this is

"""
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import writefile

n = number_of_jobs = 5
maximum_time=10

def create_job(name, delay):
    script = \
        f"""
        #BATCH ...
        #BATCH output {name}.out
        #BATCH output {name}.err
        
        # hostname
        # echo ${name}
        sleep {delay}
        """.strip()
    writefile(f"{name}.slurm")


if __name__ == '__main__':
    total = 0.0
    StopWatch.start(f"{n}-jobs")
    for i in range (100):
        name = f"job-{i}.slurm"
        t = random(0,1) * maximum_time
        total = total + t
        create_job(name, t)
        result = Shell.run(f"sbatch {name}")
        print()

    # look ofe 100 and check if all were executed
    # are all output files generated (100)

    do other stuff

    StopWatch.stop("100-jobs")
    StopWatch.nemchmark()

    print (total)