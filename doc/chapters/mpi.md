# Introduction to MPI

* What is MPI and why do you want to use it

* What are some example MPI functionalities and usage patterns (send
  receive, embarrassing parallel


### Resources

* <https://research.computing.yale.edu/sites/default/files/files/mpi4py.pdf>
* <https://www.nesi.org.nz/sites/default/files/mpi-in-python.pdf>
* <https://www.kth.se/blogs/pdc/2019/08/parallel-programming-in-python-mpi4py-part-1/>
* <http://education.molssi.org/parallel-programming/03-distributed-examples-mpi4py/index.html>
* <http://www.ceci-hpc.be/assets/training/mpi4py.pdf>
* <https://www.csc.fi/documents/200270/224366/mpi4py.pdf/825c582a-9d6d-4d18-a4ad-6cb6c43fefd8>

### Todo

* what is mpi
* Ring
* kmeans
* calculation of pi
* find number count of 8 in randome numbers between 1-10



### Installation of mpi4py on Windows

1. Look up msmpi and click the second link to download and install

   > ```
   > msmpisetup.exe
   > msmpisdk.msi`
   > ```
   > 
3. Open the system control panel

4. Click on Advanced system settings and then Environment Variables

5. Under the user variables box click on Path

6. Click New in order to add `C:\Program Files (x86)\Microsoft SDKs\MPI` and
`C:\Program Files\Microsoft MPI\Bin` to Path

7. Close any open bash windows and then open a new one

8. Type the command `which mpiexec`

9. Install mpi4py with `pip install mpi4py`

10. In order to verify that the installation worked type  `mpiexec -n 4 python mpi4py.bench helloworld`

## Installing mpi4py in a Raspberry Pi


1. Activate our virtual environment: 
   
    > ```bash
    > $ python -m venv ~/ENV3
    > $ source ~/ENV3/bin/activate
    > ```
   
2. Install Open MPI in your pi by entering the following command:
   
   > ```
   > sudo apt-get install openmpi-bin
   > ```

   After installation is complete you can check if it was successful
   by using 
   
   > ```
   > mpicc --showme:version
   > ```

3. Enter 
   
   > ```
   > pip install mpi4py
   > ``` 
    
   to download and install mpi4py.

4. The installation can be tested with `mpiexec -n 4 python -m
   mpi4py.bench helloworld` (depending on the number of cores/nodes
   available to you, it may be necessary to reduce the number of
   copies that follow the -n option) In a PI4, the previous test
   returned:
   
   > ```
   > (ENV3) pi@red:~ $ mpiexec -n 4 python -m mpi4py.bench helloworld
   > Hello, World! I am process 0 of 4 on red.
   > Hello, World! I am process 1 of 4 on red.
   > Hello, World! I am process 2 of 4 on red.
   > Hello, World! I am process 3 of 4 on red.
   > ```
   
## Installing mpi4py in MacOS
   
A similar process can be followed to install mpi4py in MacOS. In this
case, we can use Homebrew to get Open MPI by entering: 

```
$ brew install open-mpi
```
   
Once Open MPI is working, steps 3 and 4 from the  PI4
installation can be followed in order to download and install mpi4py.

## Hello World

To test if it works a build in test program is available.

To run it on on a single host with n cores (lest assume you have 2
cores), you can use:

> ```
> mpiexec -n 4 python -m mpi4py.bench helloworld
> Hello, World! I am process 0 of 5 on localhost.
> Hello, World! I am process 1 of 5 on localhost.
> Hello, World! I am process 2 of 5 on localhost.
> Hello, World! I am process 3 of 5 on localhost.
> ```

Note that the messages can be in different order.


To run it on mulitple hosts with each having n cores please create a
hostfile as follows:

TODO:


## Machine file, hostfile, rankfile


Run sudo apt-get install -y python-mpi4py on all nodes.

Test the installation: mpiexec -n 5 python -m mpi4py helloworld

THIS CAN BE DONE BEST WITH CLOUDMESH

FIRTS TEST BY HAND

TODO: VERIFY 

> ```
> mpirun.openmpi \
>   -np 2 \
>   -machinefile /home/pi/mpi_testing/machinefile \
>   python helloworld.py
> ```
 
The machinefile contains the ipaddresses

> ```
> pi@192. ....
> yout add teh ip addresses
> ```

TODO: learn about and evaluate and test if we can do 

> ```
> mpirun -r my_rankfile --report-bindings ... 
> 
> Where the rankfile contains:
> rank 0=compute17 slot=1:0
> rank 1=compute17 slot=1:1
> rank 2=compute18 slot=1:0
> rank 3=compute18 slot=1:1
> ```

## MPI Functionality examples

## MPI Collective Communication functionality examples

### Broadcast `comm.bcast()`

In this example, we broadcast a two-entry Python dictionary from a
root process to the rest of the processes in our communicator group.

> ``` python
> !include ../examples/broadcast.py
> ```

After running `mpiexec -n 4 python bcast.py` we get the following:

> ```
> before broadcast, data on rank 0 is
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> before broadcast, data on rank 1 is  None
> before broadcast, data on rank 2 is  None
> before broadcast, data on rank 3 is  None
> after broadcast, data on rank 0 is
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> after broadcast, data on rank 1 is
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> after broadcast, data on rank 2 is
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> after broadcast, data on rank 3 is
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> ```
As we can see, the process with rank 1, received the data broadcast from rank 0.


#### Scatter `comm.scatter()`

In this example, with scatter the members of a list among the
processes in the communicator group.

> ``` python
> !include ../examples/scatter.py
> ```

Executing `mpiexec -n 4 python scatter.py` yields:

> ```
> before scattering, data on rank 2 is  None
> before scattering, data on rank 3 is  None
> before scattering, data on rank 0 is  [1, 4, 9, 16]
> before scattering, data on rank 1 is  None
> data for rank 2 is  9
> data for rank 1 is  4
> data for rank 3 is  16
> data for rank 0 is  1
> ```
 
The members of the list from process 0 have been successfully
scattered among the rest of the processes in the communicator group.


#### Gather `comm.gather()`

In this example, data from each process in the communicator group is
gathered in the process with rank 0.


> ``` python
> !include ../examples/gather.py
> ```

Executing `mpiexec -n 4 python gather.py` yields:

> ```
> before gathering, data on rank 2 is  9
> before gathering, data on rank 3 is  16
> before gathering, data on rank 0 is  1
> before gathering, data on rank 1 is  4
> after gathering, data in rank 2 is  None
> after gathering, data in rank 1 is  None
> after gathering, data in rank 3 is  None
> after gathering, process 0's data is  [1, 4, 9, 16]
> ```

The data from processes with rank `1` to `size - 1` have been
successfully gathered in process 0.


#### Broadcasting buffer-like objects `comm.Bcast()`

In this example, we broadcast a NumPy array from process 0 to the rest
of the processes in the communicator group.

> ``` python
> !include ../examples/broadcast_buffer.py
> ```

Executing `mpiexec -n 4 python npbcast.py` yields:

> ```
> before broadcasting, data for rank 1 is:  [0 0 0 0 0 0 0 0 0 0]
> before broadcasting, data for rank 2 is:  [0 0 0 0 0 0 0 0 0 0]
> before broadcasting, data for rank 3 is:  [0 0 0 0 0 0 0 0 0 0]
> before broadcasting, data for rank 0 is:  [0 1 2 3 4 5 6 7 8 9]
> after broadcasting, data for rank 0 is:  [0 1 2 3 4 5 6 7 8 9]
> after broadcasting, data for rank 2 is:  [0 1 2 3 4 5 6 7 8 9]
> after broadcasting, data for rank 3 is:  [0 1 2 3 4 5 6 7 8 9]
> after broadcasting, data for rank 1 is:  [0 1 2 3 4 5 6 7 8 9]
> ```
 
As we can see, the values in the array at process with rank 0 have
been broadcast to the rest of the processes in the communicator group.


#### Scattering buffer-like objects `comm.Scatter()`

In this example, we scatter a NumPy array among the processes in the
communicator group.

> ``` python
> !include ../examples/scatter_buffer.py
> ```

Executing `mpiexec -n 4 python npscatter.py` yields:

> ```
> recvbuf in  1:  [0 0 0 0 0 0 0 0 0 0]
> recvbuf in  2:  [0 0 0 0 0 0 0 0 0 0]
> recvbuf in  3:  [0 0 0 0 0 0 0 0 0 0]
> sendbuf in 0:  [[0 0 0 0 0 0 0 0 0 0]
>                 [1 1 1 1 1 1 1 1 1 1]
>                 [2 2 2 2 2 2 2 2 2 2]
>                 [3 3 3 3 3 3 3 3 3 3]]
> recvbuf in  0:  [0 0 0 0 0 0 0 0 0 0]
> Buffer in process 2 contains:  [2 2 2 2 2 2 2 2 2 2]
> Buffer in process 0 contains:  [0 0 0 0 0 0 0 0 0 0]
> Buffer in process 3 contains:  [3 3 3 3 3 3 3 3 3 3]
> Buffer in process 1 contains:  [1 1 1 1 1 1 1 1 1 1]
> ```

As we can see, the values in the 2-D array at process with rank 0,
have been scattered among all our processes in the communicator group,
based on their rank value.


#### Gathering buffer-like objects `comm.Gather()`

In this example, we gather a NumPy array from the processes in the
communicator group into a 2-D array in process with rank 0.

> ``` python
> !include ../examples/gather_buffer.py
> ```
       
Executing `mpiexec -n 4 python npgather.py` yields:

> ```
> Buffer in process 2 before gathering:  [2 2 2 2 2 2 2 2 2 2]
> Buffer in process 3 before gathering:  [3 3 3 3 3 3 3 3 3 3]
> Buffer in process 0 before gathering:  [0 0 0 0 0 0 0 0 0 0]
> Buffer in process 1 before gathering:  [1 1 1 1 1 1 1 1 1 1]
> recvbuf in process 0 before gathering:
>  [[0 0 0 0 0 0 0 0 0 0]
>   [0 0 0 0 0 0 0 0 0 0]
>   [0 0 0 0 0 0 0 0 0 0]
>   [0 0 0 0 0 0 0 0 0 0]]
> recvbuf in process 0 after gathering: 
>  [[0 0 0 0 0 0 0 0 0 0]
>   [1 1 1 1 1 1 1 1 1 1]
>   [2 2 2 2 2 2 2 2 2 2]
>   [3 3 3 3 3 3 3 3 3 3]]
> ```

The values contained in the buffers from the different processes in
the group have been gathered in the 2-D array in process with rank 0.


#### send receive

TODO

#### Dynamic Process Management with `spawn`

In this example, we have two python programs, the first one being the manager and the second
being the worker.

> ``` python
> !include ../examples/spawn/manager.py
> ```

> ``` python
> !include ../examples/spawn/worker.py
> ```

To execute the example please go to the examples directoy and run the manager
program

> ```
> $ cd examples/spawn
> $ mpiexec -n 4 python manager.py
> ```

This will result in:

> ```
> N: 100 rank: 4
N: 100 rank: 1
N: 100 rank: 3
N: 100 rank: 2
Hello
b and rank: 0
c
d
3.1416009869231245
N: 100 rank: 0
N: 100 rank: 1
N: 100 rank: 4
N: 100 rank: 3
N: 100 rank: 2
Hello
b and rank: 0
c
d
3.1416009869231245
N: 100 rank: 0
> ```

This output depends on which child process is received first. The output can vary.

>> WARNING: There is uncertainty as to why the program does not exit out. To kill the program make sure to Ctrl-C after executing.



#### task processing (spawn, pull, …)


TODO: Cooper

##### Futures

<https://mpi4py.readthedocs.io/en/stable/mpi4py.futures.html>

#### examples for other collective communication methods

TODO

## MPI-IO

TODO: Agnes

### Collective I/O with NumPy arrays

TODO: Agnes

### Non-contiguous Collective I/O with NumPy arrays and datatypes

TODO: Agnes


## Monte Carlo calculation of Pi

TODO: Shannon, improve

TODO WHAT IS THE PROBLEM GOAL

We start with the Mathematical formulation of the Monte Carlo
calulation of pi. For each quadrant of the unit square, the area is
pi.  Therefore, the ratio of the area outside of the circle is pi over
four.  With this in mind, we can use the Monte Carlo Method for the
calculation of pi.

TODO: Drawing

TODO: HOW AND WHY DO WE NEED MULTIPLE COMPUTERS

### Program

TODO: Shannon



* Example program to run Montecarlo on multiple hosts

* Benchmarking of the code
  * cloudmesh.common (not thread safe, but still can be used, research how to use it in multiple threads)
  * other strategies to benchmark, you research (only if really needed
* Use numba to speed up the code
  * describe how to install
* showcase basic usage on our monte carlo function
* display results with matplotlib


## GPU Programming with MPI

Only possibly for someone with GPU (contact me if you do) Once we are
finished with MPI we will use and look at python dask and other
frameworks as well as rest services to interface with the mpi
programs. This way we will be able to expose the cluster to anyone and
they do not even know they use a cluster while exposing this as a
single function … (edited)

The github repo is used by all of you to have write access and
contribute to the research effort easily and in parallel.  You will
get out of this as much as you put in. Thus it is important to set
several dedicated hours aside (ideally each week) and contribute your
work to others.

It is difficult to asses how long the previous task takes as we just get
started and we need to learn first how we work together as a team. If
I were to do this alone it may take a week, but as you are less
experienced it would likely take longer. However to decrease the time
needed we can split up work and each of you will work on a dedicated
topic (but you can still work in smaller teams if you desire). We will
start assigning tasks in github once this is all set up.

Idea:

WE WILL NO LONGER USE HACKMD AS GITHUB IS BETTER FOR INTEGRATION WITH
CODE

* tutorial about hackmd.io <https://hackmd.io/t9SkKiSLR5qW9RUUA_CT-A>
* Github vs hackmd

We will use initially hackmd so we avoid issues with github and we can
learn github once we do more coding.
