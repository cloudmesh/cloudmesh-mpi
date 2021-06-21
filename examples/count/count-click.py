# Run with
#
# mpiexec -n 4 python count-click.py --n 10 --max_number 3
#

# TODO
# how do you generate a random number
# how do you generate a list of random numbers
# how do you find the number 8 in a list
# how do you gather the number 8
import os
import random

from mpi4py import MPI
import click
from cloudmesh.common.StopWatch import StopWatch
# Getting the input values or set them to a default

@click.command()
@click.option('--n', default=20, help='Number of numbers per processor')
@click.option('--max_number', default=10, help="values are between 1 and max_number")
@click.option('--find', default=8, help="the number to find")
@click.option('--verbose', default=False, help="print the values on the processor")
@click.option('--sysinfo', default=False, help="print sysinfo")
def run(n,max_number, find, verbose,sysinfo):

    # Communicator
    comm = MPI.COMM_WORLD


    # Number of processes in the communicator group
    size = comm.Get_size()

    # Get the rank of the current process in the communicator group
    rank = comm.Get_rank()

    if rank == 0:
        StopWatch.start(f"Result: {n}")

    # Each process gets different data, depending on its rank number
    data = []
    for i in range(n):
        r = random.randint(1, max_number)
        data.append(r)
    count = data.count(find)

    # Print data in each process
    if verbose:
        print(rank, count, data)

    # Gathering occurs
    count_data = comm.gather(count, root=0)

    # Process 0 prints out the gathered data, rest of the processes
    # print their data as well
    if rank == 0:

        total = sum(count_data)
        overall = size * n
        e = int(1 / max_number * overall)
        p = total/overall
        StopWatch.stop(f"Result: {n}")

        StopWatch.message(f"Result: {n}",
                          f"{total} {overall} {n} {find}")
        t = StopWatch.get(f"Result: {n}")

        print(rank, count_data)
        print(f"Total number of {find}'s: n={total} E={e} p={p} t={t}s")

        StopWatch.benchmark(sysinfo=sysinfo)

if __name__ == '__main__':
    run()