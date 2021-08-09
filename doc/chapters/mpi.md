# Introduction to MPI

* What is MPI and why do you want to use it

* What are some example MPI functionalities and usage patterns (send
  receive, embarrassing parallel)


## MPI

- [ ] TODO: Open, what is mpi <https://github.com/cloudmesh/cloudmesh-mpi/issues/19>

Message Passing Interface (MPI) is a message-passing standard that allows for efficient
communication of data between the address spaces of multiple processes. Work on the
creation of the standard began in 1992 as a collective effort undertaken by several
organizations, institutions, vendors and users. Since the presentation of the first draft
in November of 1993, the standard has undergone several revisions and updates leading to its
current version: MPI 4.0 (June 2021).

MPI is a specification, meaning that there can be multiple implementations of the standard.
Examples of popular implementations are MPICH and Open MPI, although many other free or
commercial implementations exist.

Additionally, MPI is a language-independent interface. Although support for C and Fortran is
included as part of the standard, multiple libraries providing bindings fot other languages
are available, including those for Java, Julia, R, Ruby and Python.

Thanks to its standardized nature, the portability and scalability it provides, and to the
many available implementations, MPI is a popular tool in the creation of high performance
and parallel computing programs.


- [ ] TODO: Open, Ring <https://github.com/cloudmesh/cloudmesh-mpi/issues/15>
- [ ] TODO: Open, calculation of pi <https://cvw.cac.cornell.edu/python/exercise>
  <https://github.com/cloudmesh/cloudmesh-mpi/projects/1?card_filter_query=monte>

Maybe to complex:

- [ ] TODO: Open, k-means there may be others <https://medium.com/@hyeamykim/parallel-k-means-from-scratch-2b297466fdcd>


## Prerequisite

For the examples listed in this document, it is important to know the number of
cores in your computer. This can be found out through the command line or a python program.

In Python, you can do it with 

> ```python
> import multiprocessing
> multiprocessing.cpu_count()
> ```

or as a command line 

> ```bash
> $ python -c "import multiprocessing;  print(multiprocessing.cpu_count())"
> ```

Alternatively, you can  use the following

Linux: 

> ```bash
> $ nproc
> ```

macOS: 

> ```bash
> $ sysctl hw.physicalcpu hw.logicalcpu
> ```


Windows: 

> ```bash
> $ wmic CPU Get DeviceID,NumberOfCores,NumberOfLogicalProcessors
> ```


## Installation


### Installation of mpi4py on Windows


1. First you need to download msmpi from

   *
   <https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi#ms-mpi-downloads>
   
   Go to the download link underneath the heading `MS-MPI Downloads`
   and download and install it. Select the two packages and click 
   Next. When downloaded, click on them and complete the setups.

   > ```
   > msmpisetup.exe
   > msmpisdk.msi
   > ```

2. Open the system control panel and click on `Advanced system settings` (which
   can be searched for with the search box in the top-right, and then click
   `View advanced system settings`) and then click `Environment Variables...`

3. Under the user variables box click on `Path`

4. Click New in order to add `C:\Program Files (x86)\Microsoft SDKs\MPI` and
   `C:\Program Files\Microsoft MPI\Bin` to the Path. The `Browse Directory...`
   button makes this easier and the `Variable name` can correspond to each
   directory, e.g. "MPI" and "MPI Bin" respectively

5. Close any open bash windows and then open a new one

6. Type the command

   > ```bash
   > $ which mpiexec
   > ```

   to verify if it works.

7. After you verified it is available, install mpi4py with

   > ```bash
   > $ pip install mpi4py
   > ```

   ideally while bash is in venv

8. The installation can be tested with `mpiexec -n 4 python -m
   mpi4py.bench helloworld` (depending on the number of cores/nodes
   available to you, it may be necessary to reduce the number of
   copies that follow the -n option):
   
   > ```
   > (ENV3) pi@red:~ $ mpiexec -n 4 python -m mpi4py.bench helloworld
   > Hello, World! I am process 0 of 4 on red.
   > Hello, World! I am process 1 of 4 on red.
   > Hello, World! I am process 2 of 4 on red.
   > Hello, World! I am process 3 of 4 on red.
   > ```

### Installing mpi4pi on Ubuntu

The instalation of mpi4py on ubuntu is relatively easy. Please follow these steps. We recommend that you create a 
python `venv` so you do not by accident interfere with your system python. As usual you can activate it in your 
`.bashrc file while adding the source line there. Lastly, make sure you check it out and adjust the `-n` parameters 
to the number of cores of your machine.

> ```bash
> $ sudo apt install python3.9 python3.9-dev
> $ python3 -m venev ~/ENV3
> $ source `/ENV3/bin/activate`
> (ENV3) $ sudo apt-get install -y mpich-doc mpich 
> (ENV3) $ pip install mpi4py -U
> (ENV3) $ mpiexec -n 4 python -m mpi4py.bench helloworld
> > ```

### Installing mpi4py in a Raspberry Pi


1. Activate our virtual environment: 
   
    > ```bash
    > $ python -m venv ~/ENV3
    > $ source ~/ENV3/bin/activate
    > ```
   
2. Install Open MPI in your pi by entering the following command:
   
   > ```
   > $ sudo apt-get install openmpi-bin
   > ```

   After installation is complete you can check if it was successful
   by using 
   
   > ```
   > $ mpicc --showme:version
   > ```

3. Enter 
   
   > ```
   > $ pip install mpi4py
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
   
### Installing mpi4py in MacOS

A similar process can be followed to install mpi4py in macOS. In this
case, we can use Homebrew to get Open MPI floowed by installing mpi4py 
in your venv

```
$ xcode-select --install
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
$ brew install wget
$ brew install open-mpi
$ python3 -m venv ~/ENV3
$ source ~/ENV3/bin/activate
$ pip install mpi4py
```

### Installing Homebrew on MacOS

1. Download Xcode from appstore 
2. Open Terminal from Applications
3. Run:
 
   > ```bash
   > $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
   > ```

4. Enter password
5. Hit return
6. Follow instructions on screen


## Hello World

To test if it works a build-in test program is available.

To run it on on a single host with n cores (lest assume you have 2
cores), you can use:

> ```
> mpiexec -n 4 python -m mpi4py.bench helloworld
> Hello, World! I am process 0 of 5 on localhost.
> Hello, World! I am process 1 of 5 on localhost.
> Hello, World! I am process 2 of 5 on localhost.
> Hello, World! I am process 3 of 5 on localhost.
> ```

Note that the messages can be in a different order.


To run it on multiple hosts with each having n cores please create a
`hostfile` as follows:

- [ ] TODO: Open, how to run it on multiple hosts on the PI

## Ring computation using mpi4py

As an example of the use of mpi4py, we present an instance of communication between a group of processes organized in a ring. 

[Processes organized in a ring perform a sum operation]
   (https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/ring.png)

In the example, the user provides an integer that is transmitted from process with rank 0, to process with rank 1 and so on until the data returns to process 0. Each process increments the integer by 1 before transmitting it to the next one, so the final value received by process 0 after the ring is complete is the sum of the original integer plus the number of processes in the communicator group.

> ``` python
> !include ../examples/ring.py
> ```

Executing the code in the example by entering ```mpiexec -n 2 python ring.py``` in the terminal will produce the following result:

>```bash
> Communicator group with 4 processes
> Enter an integer to transmit: 6
> Process 0 transmitted value 7 to process 1
> Process 1 transmitted value 8 to process 2
> Process 2 transmitted value 9 to process 3
> Process 3 transmitted value 10 to process 0
> Final data received in process 0 after ring is completed: 10
>```
As we can see, the integer provided to process 0 (6 in this case) was successively incremented by each process in the communicator group to return a final value of 10 at the end of the ring.
 

## Machine file, hostfile, rankfile


Run 

> ```bash 
> $ sudo apt-get install -y python-mpi4py 
> ```

on all nodes.

Test the installation: 

> ```
> $ mpiexec -n 5 python -m mpi4py helloworld
>```

THIS CAN BE DONE BEST WITH CLOUDMESH

FIRTS TEST BY HAND

- [ ] TODO: Open, VERIFY 

> ```
> mpirun.openmpi \
>   -np 2 \
>   -machinefile /home/pi/mpi_testing/machinefile \
>   python helloworld.py
> ```
 
The machinefile contains the ipaddresses

> ```
> pi@192. ....
> yout add the ip addresses
> ```

- [ ] TODO: Open, learn about and evaluate and test if we can do 

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

There are some differences between mpi4py and the standard MPI implementations for C/Fortran worth noting.

In mpi4py, the standard MPI_INIT() and MPI_FINALIZE() commonly used to initialize and terminate the MPI environment are automatically handled after importing the mpi4py module.
Although not generally advised, mpi4py still provides MPI.Init() and MPI.Finalize() for users interested in manually controlling these operations. Additionally, the automatic
initialization and termination can be deativated. For more information on this topic, please check the following links:

 * [MPI.Init() and MPI.Finalize()](https://githubmemory.com/repo/mpi4py/mpi4py/issues/54)
 * [Deactivating automatic initialization and termination on mpi4py](https://bitbucket.org/mpi4py/mpi4py/issues/85/manual-finalizing-and-initializing-mpi)

Another characteristic feature of mpi4py is the availablitly of uppercase and lowercase communication methods. Lowercase methods like `comm.send()` use Python's `pickle`
module to transmit objects in a serialized manner. In contrast, the uppercase versions of methods like `comm.Send()` enable transmission of data contained in a contiguous
memory buffer, as featured in the MPI standard. For additional information on the topic, check (https://mpi4py.readthedocs.io/en/stable/overview.html?highlight=pickle#communicating-python-objects-and-array-data).

## MPI Point-to-Point Communication Examples

### Sending/Receiving

The `send()` and `recv()` methods provide for functionality to transmit data
between two specific processes in the communicator group.


[Sending and receiving data between two processes] (https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/send_receive.png)

Here is the definition for the `send()` method:

> ```
> comm.send(buf, dest, tag)
> ```

`buf` represents the data to be transmitted, `dest` and `tag` are integer
values that specify the rank of the destination process, and a tag to identify
the message being passed, respectively. `tag` is particularly useful for cases
when a process sends multiple kinds of messages to another process.

In the other end is the `recv()` method, with the following definition:

> ```
> comm.recv(buf, source, tag, status)
> ```    

In this case, `buf` can specify the location for the received data to be
stored. In more recent versions of MPI, 'buf' has been deprecated. In those cases,
we can simply assign `comm.recv(source, tag, status)` as the value of our buffer
variable in the receiving process. Additionally, `source` and `tag` can specify
the desired source and tag of the data to be received. They can also be set to
`MPI.ANY_SOURCE` and `MPI.ANY_TAG`, or be left unspecified.

In the following example, an integer is transmitted from process 0 to process 1.

> ``` python
> !include ../examples/send_receive.py
> ```

Executing `mpiexec -n 4 python send_receive.py` yields:

> ```bash
> After send/receive, the value in process 2 is None
> After send/receive, the value in process 3 is None 
> After send/receive, the value in process 0 is None
> After send/receive, the value in process 1 is 42
> ```

As we can appreciate, transmission only occurred between processes 0 and 1, and
no other process was affected.

The following example illustrates the use of the uppercase versions of the methods
`comm.Send()` and `comm.Recv()` to perform a buffered transmission of data between
processes 0 and 1 in the communicator group.

>```python
> !include ../examples/send_receive_buffer.py
> ```

Executing `mpiexec -n 4 python send_receive_buffer.py` yields:

> ```bash
> After Send/Receive, the value in process 3 is [0 0 0 0 0]
> After Send/Receive, the value in process 2 is [0 0 0 0 0]
> After Send/Receive, the value in process 0 is [0 0 0 0 0]
> After Send/Receive, the value in process 1 is [1 2 3 4 5]
> ```

Lastly, an example of the non-blocking send and receive methods `comm.isend()` and
`comm.irecv()`. Non-blocking versions of these methods allow for the processes involved
in transmission/reception of data to perform other operations in overlap with the
communication. In contrast, the blocking versions of these methods previously
exemplified do not allow data buffers involved in transmission or reception of data to
be accessed until any ongoing communication involving the particular processes has been
finalized.

>```python
> !include ../examples/isend_ireceive.py
> ```

Executing `mpiexec -n 4 python isend_ireceive.py` yields:

> ```bash
> After isend/ireceive, the value in process 2 is None
> After isend/ireceive, the value in process 3 is None
> After isend/ireceive, the value in process 0 is None
> After isend/ireceive, the value in process 1 is 42
> ```

## MPI Collective Communication Examples

### Broadcast

The `bcast()` method and it is buffered version `Bcast()` broadcast a message
from a specified "root" process to all other processes in the communicator
group.

In terms of syntax, `bcast()` takes the object to be broadcast and the
parameter `root`, which establishes the rank number of the process broadcasting
the data. If no root parameter is specified, `bcast` will default to
broadcasting from the process with rank 0.

In this example, we broadcast a two-entry Python dictionary from a root process
to the rest of the processes in the communicator group.

![Broadcasting data from a root process to the rest of the processes in the communicator group](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/bcast.png)

The following code snippet shows the creation of the dictionary in process with
rank 0. Notice how the variable `data` remains empty in all the other
processes.

> ``` python
> !include ../examples/broadcast.py
> ```

After running `mpiexec -n 4 python broadcast.py` we get the following:

> ```
> before broadcast, data on rank 3 is: None
> before broadcast, data on rank 0 is: 
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> before broadcast, data on rank 1 is: None
> before broadcast, data on rank 2 is: None
> after broadcast, data on rank 3 is: 
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> after broadcast, data on rank 0 is: 
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> after broadcast, data on rank 1 is: 
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> after broadcast, data on rank 2 is: 
>   {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
> ```

As we can see, all other processes received the data broadcast from the root process.

In our next example, we broadcast a NumPy array from process 0 to the rest
of the processes in the communicator group using the uppercase `comm.Bcast()` method.

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
 
As we can see, the values in the array at the process with rank 0 have
been broadcast to the rest of the processes in the communicator group.


#### Scatter

- [ ] TODO: Fidel, explanation is missing

In this example, with `scatter` the members of a list among the
processes in the communicator group.

- [ ] TODO: All, add images

![Example to scatter data to different processors from the one with rank 0](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/scatter.png)

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

In the following example, we scatter a NumPy array among the processes in the
communicator group by using the uppercase version of the method `comm.Scatter()`.

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

#### Gather

- [ ] TODO: Fidel, explenation is missing

In this example, data from each process in the communicator group is
gathered in the process with rank 0.

![Example to gather data to different processors from the one with rank 0](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/gather.png)



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

The example showcases the use of the uppercase method `comm.Gather()`.
NumPy arrays from the processes in the communicator group are gathered
into a 2-D array in process with rank 0.

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

#### Gathering buffer-like objects in all processes

In this example, each process in the communicator group computes and
stores values in a NumPy array (row). For each process, these values
correspond to the multiples of the process' rank and the integers in
the range of the communicator group's size. After values have been
computed in each process, the different arrays are gathered into a 2D
array (table) and distributed to ALL the members of the communicator group
(as opposed to a single member, which is the case when `comm.Gather()` is
used instead).

![Example to gather the data from each process into ALL of the processes in the group](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/allgather.png)

> ```python
> !include ../examples/allgather_buffer.py
> ```

Executing 

> ```
> $ mpiexec -n 4 python allgather_buffer.py
> ```

results in the output 

> ```
> Process 1 table before Allgather:  [[0. 0.]
>  [0. 0.]] 
> 
> Process 0 table before Allgather:  [[0. 0.]
>  [0. 0.]] 
>
> Process 1 table after Allgather:  [[0. 0.]
>  [0. 1.]] 
> 
> Process 0 table after Allgather:  [[0. 0.]
>  [0. 1.]] 
> ```

As we see, after `comm.Allgather()` is called, every process gets a copy
of the full multiplication table.


#### Dynamic Process Management with `spawn`

Using
> ``` python
> MPI.Comm_Self.Spawn
> ```

will create a child process that can communicate with the parent. In the spawn code example, the manager broadcasts an array to the worker.

In this example, we have two python programs, the first one being the
manager and the second being the worker.

![Example to spawn a program and start it on the different processors from the one with rank 0](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/spawn.png)


> ``` python
> !include ../examples/spawn/manager.py
> ```

> ``` python
> !include ../examples/spawn/worker.py
> ```

To execute the example please go to the examples directory and run the manager
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

> `WARNING:` When running this program it may not terminate. To
>terminate use for now `CTRL-C`.



#### task processing (spawn, pull, ...)


- [ ] TODO: Cooper, spawn, pull

##### Futures

- [ ] TODO: Open, futures

<https://mpi4py.readthedocs.io/en/stable/mpi4py.futures.html>

#### Examples for other collective communication methods

- [ ] TODO: Agness, introduction

## MPI-IO

- [ ] TODO: Agness, MPI-IO

### Collective I/O with NumPy arrays
How to use Numpy with MPI
1. Download Numpy with `pip install numpy` in a terminal
2. `import numpy as np` to use numpy in the program
3. Advantages of numpy over lists
   - Numpy stores memory contiguously
   - Uses a smaller number of bytes 
   - Can multiply arrays by index
   - It’s faster
   - Can store different data types including images
   - Contains random number generators

Numpy syntax
1. To define an array type: `np.nameofarray([1,2,3])`
2. To get the dimension of the array: `nameofarray.ndim`
3. To get the shape of the array (the number of rows and columns): `nameofarray.shape`
4. To get the type of the array: `nameofarray.dtype`
5. To get the number of bytes: `nameofarray.itemsize`
6. To get the number of elements in the array: `nameofarray.size`
7. To get the total size: `nameofarray.size * nameofarray.itemsize`

- [ ] TODO: Agness - IO and Numpy


### Non-contiguous Collective I/O with NumPy arrays and datatypes

- [ ] TODO: Agness, noncontigious IO


## Monte Carlo calculation of Pi

- [ ] TODO: Open, improve

- [ ] TODO: Open  WHAT IS THE PROBLEM GOAL

We start with the Mathematical formulation of the Monte Carlo
calculation of pi. For each quadrant of the unit square, the area is
pi.  Therefore, the ratio of the area outside of the circle is pi over
four.  With this in mind, we can use the Monte Carlo Method for the
calculation of pi.

> ``` python
> !include ../examples/monte-carlo/montecarlo.py
> ```

- [ ] TODO: Open, Drawing

- [ ] TODO: Open, HOW AND WHY DO WE NEED MULTIPLE COMPUTERS

### Program

- [ ] TODO: Open, PI Montecarlo


- [ ] TODO: Open, Example program to run Montecarlo on multiple hosts

- [ ] TODO: Open, Benchmarking of the code

Use for benchmarking
* cloudmesh.common (not thread-safe, but still can be used, research how to 
  use it in multiple threads)
  * other strategies to benchmark, you research (only if really needed
* Use numba to speed up the code
  * describe how to install
* showcase basic usage on our monte carlo function
* display results with matplotlib

### Counting Numbers

The following program generates arrays of random numbers each 20 (n)
  in length with the highest number possible being 10 (max_number).
  It then uses a function called count() to count the number of 8's in
  each data set.  The number of 8's in each list is stored count_data.
Count_data is then summed and printed out as the total number of 8's.

> ``` python
> !include ../examples/count/count.py
> ```

Executing `mpiexec -n 4 python count.py` gives us:

>
> 1 1 [7, 5, 2, 1, 5, 5, 5, 4, 5, 2, 6, 5, 2, 1, 8, 7, 10, 9, 5, 6]
> 
> 3 3 [9, 2, 9, 8, 2, 7, 7, 2, 10, 1, 2, 5, 3, 5, 10, 8, 10, 10, 8, 10]
> 
> 2 3 [1, 3, 8, 5, 7, 8, 4, 2, 8, 5, 10, 7, 10, 1, 6, 5, 9, 6, 6, 7]
> 
> 0 3 [6, 9, 10, 2, 4, 8, 8, 9, 4, 1, 6, 8, 6, 9, 7, 5, 5, 6, 3, 4]
> 
> 0 [3, 1, 3, 3]
> 
> Total number of 8's: 10
>

## GPU Programming with MPI

Only possibly for someone with GPU (contact me if you do) Once we are
finished with MPI we will use and look at python dask and other
frameworks as well as rest services to interface with the MPI
programs. This way we will be able to expose the cluster to anyone and
they do not even know they use a cluster while exposing this as a
single function … (edited)

The Github repo is used by all of you to have write access and
contribute to the research effort easily and in parallel.  You will
get out of this as much as you put in. Thus it is important to set
several dedicated hours aside (ideally each week) and contribute your
work to others.

It is difficult to assess how long the previous task takes as we just get
started and we need to learn first how we work together as a team. If
I were to do this alone it may take a week, but as you are less
experienced it would likely take longer. However, to decrease the time
needed we can split up work and each of you will work on a dedicated
topic (but you can still work in smaller teams if you desire). We will
start assigning tasks in GitHub once this is all set up.

## Python Ecosystem

It is possible to pass parameters from Git Bash into a Python environment
using os.environ and a shell file.


> ``` python
> !include ../examples/parameters/environment-parameter.py
> ```

Ensure that this code is saved in a particular directory. Then create a
shell file named run.sh with the following contents:

```python
$ N=1; python environment-parameter.py
$ N=2; python environment-parameter.py
```

Save the following py file in the same directory as well:
> ``` python
> !include ../examples/parameters/click-parameter.py
> ```

You must cd (change directory) into the directory with all of these 
files in Git Bash. Input the following commands into Git Bash:

```
# This command creates an environment variable called N
$ export N=10
# This command prints the environment variable called N
$ echo $N
# This command launches a Python environment
$ python -i
>>> import os
>>> os.environ["N"]
>>> exit()
$ python environment-parameter.py
$ sh run.sh
$ sh run.sh | fgrep "csv,processors"
$ python click-parameter.py
# You can manually set the variable in git bash in the same line as you open the .py file
$ python click-parameter.py --n=3
```

## Resources MPI

* <https://research.computing.yale.edu/sites/default/files/files/mpi4py.pdf>
* <https://www.nesi.org.nz/sites/default/files/mpi-in-python.pdf>
* <https://www.kth.se/blogs/pdc/2019/08/parallel-programming-in-python-mpi4py-part-1/>
* <http://education.molssi.org/parallel-programming/03-distributed-examples-mpi4py/index.html>
* <http://www.ceci-hpc.be/assets/training/mpi4py.pdf>
* <https://www.csc.fi/documents/200270/224366/mpi4py.pdf/825c582a-9d6d-4d18-a4ad-6cb6c43fefd8>


