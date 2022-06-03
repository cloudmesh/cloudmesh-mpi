import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()
assert comm.size == 2

if comm.rank == 0:
    sendmsg = 777
    print("0", sendmsg)
    comm.send(sendmsg, dest=1, tag=77)
    recvmsg = comm.recv(source=1, tag=55)
    print("0", sendmsg)
else:
    recvmsg = comm.recv(source=0, tag=77)
    sendmsg = "abc"
    comm.send(sendmsg, dest=0, tag=55)
print(sendmsg)