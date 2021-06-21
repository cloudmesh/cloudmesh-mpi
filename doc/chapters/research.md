## Hardware Considerations

Describes and summarizes what hardware you could use

### Backup

When you rock on a research project you may install programs on your
computer that's me cause problems at a later time. The work we do yes
research and not production. Hence, we need to be assuring that you
have a backup strategy in place before you work on your research
activities.

For that reason, we recommend that you purchase an external backup
drive that you use regularly to create backups from you are
System. The best Open backup solutions Orissa back up trash include
multiple redundant drives so that if even the backup fails you can
recover easily from a failure. An external backup drive is relatively
inexpensive and you can easily order them via internet vendors. To
protect yourself from a broken backup drive (this happens!) we
recommend either by at one point a second one or use a RAID-enabled
backup. Certainly your second or even primary backup could be a cloud
service such as google drive.

Alternatively and, you can use cloud storage services such as Google
Drive to back up your most important information.

Examples:

* USB Drive or External HDD enclosure with one or more disks, When
  using an SSD likely the fastest backup solution. YOU can buy also an
  external Drive bay with multiple bays and purcahse HDD or SSD drives
  based on your budget. Make sure to by one with USB3 or
  thunderbolt. The limit will be your budget.

* [TrueNas](https://www.truenas.com/) (you can build your own or get one ready made)

* [Synology](https://www.synology.com/en-us) (ready made)

* QNAS

### Bare metal on your Computer

- [ ] TODO, All see other todos 

Recommendations

* Memory (16GB)
* SSD (>512GB)

* Reasonably new computer less than 5 years of age

* Alternative culd be Raspberry PI4 with 8GB runnng Ubuntu or
  Raspberry OS for smaller projects. We have seen that some students
  had computers that cost when bought >$1K but because they were too
  old a Raspberry Pi of about $100 wass much much faster. It is up to
  you to make a decission which hardware you like to use. To get
  started with clusters and parallel computing ranging from MPI,
  Hadoop, SPark and containers a Raspberry PI cluster is not a bad
  choice

### Using Raspberry PIs

- [ ] TODO, Open,  Using Raspberry PIs

### Laptops and Desktops

- [ ] TODO, Open, Laptops and Desktops

### Virtual Machines

- [ ] TODO, Open, using vms

requires >=16 GB on laptop/desktop

#### Multipass

- [ ] TODO: Erin, Using multipass

#### WSL2

## Installing WSL on Windows 10

WSL is a layer that allows the running of Linux executables on a Windows machine. This broadens the number of commands able to be run and creates more flexibility.

To install WSL2 your computer must have Hyper-V support enabled.
THis doe snot work on Windows HOmew and you need to upgrade to Windows
Pro, Edu or some other Windows 10 version that supports it. Windows
Edu is typically free for educational institutions. The HYper-V must
be enabled from your Bios and you need to change your settings if it
is not enabled.

More information about WSL is provided at

* <https://docs.microsoft.com/en-us/windows/wsl/install-win10> for further detail

To install WSL2 you can follow these directions while using
Powershell as an administrative user and run

> ```
> ps$ dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
> ps$ dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
> ps$ wsl --set-default-version 2
> ```

Next, Download Ubuntu 20.04 LTS from the Microsoft store

* <https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab>

Run Ubuntu and create a username and passphrase.

Make sure not to just give an empty passphrase but chose a secure one.

#### Make

# Make on Windows

Make fires provide a good feature to organize workflow while
assembling programs or documents to create an integrated document.
Within makefiles defined targets that you can call and are executed.
Through its mechanism, it can easily deal with complex workflows that
require a multitude of actions to be executed. Makefiles are executed
by the program make that is available on all platforms.

On machines such as on machines that run Linux, it is likely to be
pre-installed while on MacOS you can install it with Xcode. On
Windows, you have to explicitly install it and we recommend that you
use get bashed the window so that you can call make from us and get
bash. The following instructions will provide you with a guide to install
make under windows.

## Installation

Please visit

* <https://sourceforge.net/projects/ezwinports/files/>

and download the file

* ['make-4.3-without-guile-w32-bin.zip`](https://sourceforge.net/projects/ezwinports/files/make-4.3-without-guile-w32-bin.zip/download)

After the download you have to extract and unzip the file as follows:

```bash
$ cp make-4.3-without-guile-w32-bin.zip /usr
$ cd /usr
$ unzip make-4.3-without-guile-w32-bin.zip
```

Now start a new terminal and type the command

```bash
$ which make
```

It will provide you the location if the installation was successful

> ```bash
> /usr/bin/make
> ```

to make sure it is properly installed and in the correct directory.
>

#### VMs on your local computer

#### Cloud Virtual Machines

#### Campus Resources

- [ ] TODO: Erin, campus resoources

##### Indiana University

Computer and cluster at Indiana university could be alternative to
Raspberry PI cluster, but Cluster will teach you other things that you
will not experience if you use the campus cluster. You have more
access, please keep that in mind.

- [ ] TODO: Erin, list resources hera nad how to get access

## Other resoources

* very important: <https://www.ismll.uni-hildesheim.de/lehre/prakAIML-17s/script/02.MPI.pdf>
* <https://materials.jeremybejarano.com/MPIwithPython/>
* <https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html>
* <https://research.computing.yale.edu/sites/default/files/files/mpi4py.pdf>
* <https://towardsdatascience.com/parallel-programming-in-python-with-message-passing-interface-mpi4py-551e3f198053>
* machinefile: <https://pythonprogramming.net/installing-testing-mpi4py-mpi-python-tutorial/>
* size, rank: <https://pythonprogramming.net/mpi4py-size-command-mpi/>
  they have mpirun.openmpi -np 5 -machinefile /home/pi/mpi_testing/machinefile python
  so we can specify a machine file, find out how that looks liek
* jupyter on mpi <https://raspi.farm/howtos/installing-MPI-on-the-cluster/>
* <https://pythonprogramming.net/basic-mpi4py-script-getting-node-rank/>
* <https://www.nesi.org.nz/sites/default/files/mpi-in-python.pdf>

## Installation 

In this section we will quickly summarize how you install of python on
your hardware This includes

* Windows 10
* MacOs
* Raspberry (using our cms burn)

Each installation documents the install from python.org

### Instalation on Windows 10

- [ ] TODO: Cooper, instalation on windows

### Instalation on MacOS

- [ ] TODO: Agnes, instalation on Mac

### Instalation on Raspberry OS

- [ ] TODO: Open, using cms burn

### Instalation on Raspberry Ubuntu

- [ ] TODO: Open, using cms burn



