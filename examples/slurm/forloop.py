import os
count = 5
scriptname = "sort.slurm"
for i in range(count):
    os.system(f"sbatch {scriptname}")
