from mpi4py import MPI
from cloudmesh.common.StopWatch import StopWatch

StopWatch.start("MPI.COMM_WORLD")
comm = MPI.COMM_WORLD
assert comm.size == 2
StopWatch.stop("MPI.COMM_WORLD")

StopWatch.benchmark()

StopWatch.start(f"Rank {comm.rank}")
if comm.rank == 0:
    StopWatch.start(f"Rank internal 0 {comm.rank}")
    sendmsg = 777
    comm.send(sendmsg, dest=1, tag=55)
    recvmsg = comm.recv(source=1, tag=77)
    StopWatch.stop(f"Rank internal 0 {comm.rank}")
else:
    StopWatch.start(f"Rank internal n {comm.rank}")
    recvmsg = comm.recv(source=0, tag=55)
    sendmsg = "abc"
    comm.send(sendmsg, dest=0, tag=77)
    StopWatch.stop(f"Rank internal n {comm.rank}")
    
StopWatch.stop(f"Rank {comm.rank}")

StopWatch.benchmark()

print(sendmsg)
