#!/usr/bin/env python
#
# PLEASE DO NOT EDIT IT DIRECTLY ON cloudmesh.github.io
#
# Instead, if modifications are needed, modify it here
#
# * https://github.com/cloudmesh/get/blob/main/pi/slurm/index.html
#
#   curl -Ls http://cloudmesh.github.io/get/pi/slurm | python
#
# <pre>

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import banner
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.Host import Host
from cloudmesh.common.util import readfile, writefile
from cloudmesh.common.Printer import Printer
from cloudmesh.common.console import Console
from cloudmesh.common.util import yn_choice
from cloudmesh.common.Shell import Shell
from pprint import pprint
import os
import sys
import re
import textwrap
import time
import subprocess
from cloudmesh.burn.usb import USB
from cloudmesh.burn.sdcard import SDCard


# hosts = "red,red0[1-3]"
# workers = "red0[1-3]"
# manager = "red"

def hostexecute(script, manager):
    for command in script.splitlines():
        print(command)
        results = Host.ssh(hosts=manager, command=command)
        print(Printer.write(results))


def managerNamer():
    manager = subprocess.run(['hostname'],
                             capture_output=True,
                             text=True).stdout.strip()
    print(f"The hostname of the manager is taken to be {manager} \n")
    return manager


# defining function which formulates hosts variable
# the hosts variable has manager and workers

def hostsVariable(manager, workers):
    hosts = f'''{manager},{workers}'''
    hosts = str(hosts)
    return (hosts)


# read the file user_input_workers
def read_user_input_workers(manager):
    results = Host.ssh(hosts=manager, command='cat user_input_workers')
    print(Printer.write(results))
    for entry in results:
        print(str(entry["stdout"]))
        workers = str(entry["stdout"])
        return workers


# tell user to ssh back to manager on reboot and reboot
def tell_user_rebooting():
    banner('The cluster is rebooting. Wait a minute for the Pis to come '
           'back online and ssh into the manager. Then,'
           ' rerun the script by issuing "./install_slurm.py" to continue.')
    os.system("cms host reboot " + hosts)


# function that returns ip of pi
def get_IP(manager):
    results = Host.ssh(hosts=manager, command="/sbin/ifconfig eth0 | grep 'inet' | cut -d: -f2")
    print(Printer.write(results))
    for entry in results:
        print(str(entry["stdout"]))
        ipaddress = str(entry["stdout"])
    print(ipaddress)
    ipaddress2 = ipaddress.replace('inet ', '')
    print(ipaddress2)
    ipaddress3 = ipaddress2.split(' ')
    print(ipaddress3)
    ipaddress4 = [x for x in ipaddress3 if x]
    print(ipaddress4)
    trueIP = ipaddress4[0]
    print(trueIP)
    return trueIP


# function that checks to see if a step has been run


def check_step(step_number, device):
    step_number_string = str(step_number)
    just_the_step = f"step{step_number_string}"
    changed_command = f"ls step{step_number_string}"
    results = Host.ssh(hosts=device, command=changed_command)
    print(Printer.write(results))
    step_done = True
    for entry in results:
        if just_the_step in str(entry["stdout"]) and 'cannot access' in str(entry["stdout"]):
            step_done = False
            entry["stderr"] = "False"
    return step_done


def try_installing_package(command_for_package, listOfWorkers):
    for worker in listOfWorkers:
        success = False
        while not success:
            success = True
            results = Host.ssh(hosts=worker,
                               command=command_for_package)
            print(Printer.write(results))
            for entry in results:
                if ('Could not connect to' in str(entry["stdout"])) or ('Failed to fetch' in str(entry["stdout"])):
                    msg = f"The SLURM script could not install needed packages, but will try again. " \
                          f"This is expected behavior and it should fix itself within a few minutes. " \
                          f"Currently fixing {worker}."
                    banner(msg)
                    # return msg
                    success = False
                else:
                    banner(f"Package installation has succeeded for {worker}.")
            time.sleep(5)


def try_downloading_from_github(command_for_download, listOfWorkers):
    for worker in listOfWorkers:
        success = False
        while not success:
            success = True
            results = Host.ssh(hosts=worker,
                               command=command_for_download)
            print(Printer.write(results))
            for entry in results:
                if 'Failed to connect to' in str(entry["stderr"]):
                    msg = f"The SLURM script could not download needed packages, but will try again. " \
                          f"This is expected behavior and it should fix itself within a few minutes. " \
                          f"Currently fixing {worker}."
                    banner(msg)
                    # return msg
                    success = False
                else:
                    banner(f"Package download has succeeded for {worker}.")
            time.sleep(5)


# Beginning to define SLURM installation

# input
#  basename = "red"
#  no workers = "03" # "3" "01000" 00001-01000
# output
#  red000  -> red, red001, red002, red003

def step0():
    StopWatch.start("Current section time")
    banner("Welcome to SLURM Installation. Initializing preliminary steps.")
    print("We assume that you run this script on the manager Pi and that your worker naming schema is \n"
          "incremental in nature. \n")
    manager = managerNamer()
    user_input_workers = input(str('''Please enter the naming schema of your workers. For example, if you have 3 
        workers then enter "red0[1-3]". Another example for 7 workers is "worker[1-7]" (do not include
        quotation marks): \n'''))

    results = Host.ssh(hosts=manager, command="touch user_input_workers")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command=f'''echo '{user_input_workers}' >> user_input_workers''')
    print(Printer.write(results))

    # intro and asking for workers from user
    workers = read_user_input_workers(manager)

    hosts = hostsVariable(manager, workers)

    results = Host.ssh(hosts=hosts, command="touch step0")
    print(Printer.write(results))
    StopWatch.stop("Current section time")
    StopWatch.benchmark()


def step1():
    StopWatch.start("Current section time")
    # intro and asking for workers from user
    banner("Initializing Step 1 now.")
    manager = managerNamer()

    workers = read_user_input_workers(manager)

    hosts = hostsVariable(manager, workers)

    banner("Now updating packages. This may take a while.")
    results = Host.ssh(hosts=hosts, command="sudo apt-get update")
    print(Printer.write(results))
    # parallel_execute(hosts,"sudo apt install ntpdate -y")
    # results2 = Host.ssh(hosts=hosts, command="sudo apt install ntpdate -y")
    # print(Printer.write(results2))

    # make array with list of workers
    listOfWorkers = Parameter.expand(workers)

    print(listOfWorkers)
    listOfManager = [manager]
    try_installing_package("sudo apt install ntpdate -y", listOfManager)
    try_installing_package("sudo apt install ntpdate -y", listOfWorkers)
    results = Host.ssh(hosts=hosts, command="touch step1")
    print(Printer.write(results))
    StopWatch.stop("Current section time")
    StopWatch.benchmark()
    tell_user_rebooting()


def step2():
    StopWatch.start("Current section time")
    banner("Initializing Step 2 now.")
    manager = managerNamer()
    if not yn_choice(
            'Please insert USB storage medium into top USB 3.0 (blue) port on manager pi and press y when done'):
        Console.error("You pressed no but the script is continuing as normal...")
        return ""
    '''
    os.system('lsblk')
    if not yn_choice('Please confirm that sda1 is your USB WHICH WILL BE FORMATTED by pressing y'):
        Console.error("Terminating: User Break")
        return ""
        sys.exit()
    '''

    # executing reading of workers
    workers = read_user_input_workers(manager)

    hosts = hostsVariable(manager, workers)

    card = SDCard()
    card.info()
    USB.check_for_readers()
    print('Please enter the device path e.g. "/dev/sda" or enter no input to default to /dev/sda (remember, do not add '
          'quotation marks)')
    print('The device of the path you enter WILL BE FORMATTED and used as cluster file storage for SLURM config:')
    device = input()
    if device == '':
        device = '/dev/sda'
    print(device)
    script = textwrap.dedent(
        f"""
        sudo mkfs.ext4 -F {device}
        sudo mkdir /clusterfs
        sudo chown nobody.nogroup -R /clusterfs
        sudo chmod 777 -R /clusterfs
        """).strip()
    hostexecute(script, manager)

    # results = Host.ssh(hosts=manager, command=f"sudo mkfs.ext4 -F {device}")
    # print(Printer.write(results))
    # results = Host.ssh(hosts=manager, command="sudo mkdir /clusterfs")
    # print(Printer.write(results))
    # results = Host.ssh(hosts=manager, command="sudo chown nobody.nogroup -R /clusterfs")
    # print(Printer.write(results))
    # results = Host.ssh(hosts=manager, command="sudo chmod 777 -R /clusterfs")
    # print(Printer.write(results))

    results = Host.ssh(hosts=manager, command=f"sudo blkid {device}")
    print(Printer.write(results))
    for entry in results:
        print(str(entry["stdout"]))
        blkid = str(entry["stdout"])
    print(blkid)
    blkid2 = re.findall(r'\S+', blkid)
    print(blkid2)
    result = [i for i in blkid2 if i.startswith('UUID=')]
    print(result)
    listToStr = ' '.join(map(str, result))
    result2 = re.findall(r'"([^"]*)"', listToStr)
    result2 = " ".join(str(x) for x in result2)
    print(type(result2))
    print(result2)
    script = textwrap.dedent(
        f"""
        echo "UUID={result2} /clusterfs ext4 defaults 0 2" | sudo tee /etc/fstab -a
        sudo mount -a
        sudo chown nobody.nogroup -R /clusterfs
        sudo chmod -R 766 /clusterfs
        sudo apt install nfs-kernel-server -y
        """)
    hostexecute(script, manager)
    trueIP = get_IP(manager)
    results = Host.ssh(hosts=manager, command=f'''sudo cat /etc/exports''')
    print(Printer.write(results))
    for entry in results:
        Preexisting = False
        if f'/clusterfs {trueIP}/24(rw,sync,no_root_squash,no_subtree_check)' in str(entry["stdout"]):
            Preexisting = True
    if not Preexisting:
        command = f'echo "/clusterfs {trueIP}/24(rw,sync,no_root_squash,no_subtree_check)" | sudo tee /etc/exports -a'
        results = Host.ssh(hosts=manager,
                           command=command)
        print(Printer.write(results))

    hostexecute("sudo exportfs -a", manager)

    # make array with list of workers
    listOfWorkers = Parameter.expand(workers)

    print(listOfWorkers)
    try_installing_package("sudo apt install nfs-common -y", listOfWorkers)
    results = Host.ssh(hosts=workers, command='sudo mkdir /clusterfs')
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command='sudo chown nobody.nogroup /clusterfs')
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command='sudo chmod -R 777 /clusterfs')
    print(Printer.write(results))

    results = Host.ssh(hosts=manager, command=f'''sudo cat /etc/fstab''')
    print(Printer.write(results))
    for entry in results:
        Preexisting = False
        if f'{trueIP}:/clusterfs    /clusterfs    nfs    defaults   0 0' in str(entry["stdout"]):
            Preexisting = True
    if not Preexisting:
        results = Host.ssh(hosts=workers,
                           command=f'''echo "{trueIP}:/clusterfs    /clusterfs    nfs    defaults   0 0" | sudo tee /etc/fstab -a''')
        print(Printer.write(results))
    results = Host.ssh(hosts=hosts, command="touch step2")
    print(Printer.write(results))
    StopWatch.stop("Current section time")
    StopWatch.benchmark()
    tell_user_rebooting()


def step3():
    StopWatch.start("Current section time")
    banner("Initializing Step 3 now.")

    manager = managerNamer()
    # getting ip in case step 2 has not run
    trueIP = get_IP(manager)

    # executing reading of workers
    workers = read_user_input_workers(manager)

    hosts = hostsVariable(manager, workers)

    listOfWorkers = Parameter.expand(workers)
    print(listOfWorkers)
    print(hosts)
    listOfManager = [manager]
    trueIP = get_IP(manager)
    if not yn_choice('The script will now install virtual Python environment on each worker'
                     ' node. This is necessary to use MPI with SLURM. The process may take upwards of half an hour'
                     ' with 4 workers. Press y and Enter when ready to continue...\n'):
        Console.error("You pressed no but the script is continuing as normal...")
        return ""
    banner("This will take a while...")
    try_installing_package("sudo apt-get install python3-venv python3-wheel python3-dev build-essential -y",
                           listOfWorkers)
    results = Host.ssh(hosts=workers, command='python3 -m venv ~/ENV3')
    print(Printer.write(results))
    try_installing_package("sudo apt-get install openmpi-bin -y", listOfWorkers)
    results = Host.ssh(hosts=workers, command='ENV3/bin/pip install mpi4py')
    print(Printer.write(results))
    try_installing_package("sudo apt install libevent-dev autoconf git libtool flex libmunge-dev munge -y",
                           listOfManager)
    try_installing_package("sudo apt install libevent-dev autoconf git libtool flex libmunge-dev munge -y",
                           listOfWorkers)
    results = Host.ssh(hosts=hosts, command='sudo mkdir -p /usr/lib/pmix/build/2.1 /usr/lib/pmix/install/2.1')
    print(Printer.write(results))
    try_downloading_from_github("cd /usr/lib/pmix && sudo git clone https://github.com/openpmix/openpmix.git source "
                                "&& cd source/ && git branch -a && sudo git checkout v2.1 && "
                                "sudo git pull", listOfManager)
    script = textwrap.dedent(
        f"""
            sudo systemctl status nfs-server.service
            sudo systemctl start nfs-server.service
            sudo mount -a
            """)
    hostexecute(script, manager)
    results = Host.ssh(hosts=hosts, command="touch step3")
    print(Printer.write(results))
    StopWatch.stop("Current section time")
    StopWatch.benchmark()
    tell_user_rebooting()

def step4():
    StopWatch.start("Current section time")
    banner("Initializing Step 4 now.")

    manager = managerNamer()
    # getting ip in case step 2 has not run
    trueIP = get_IP(manager)

    # executing reading of workers
    workers = read_user_input_workers(manager)

    hosts = hostsVariable(manager, workers)

    listOfWorkers = Parameter.expand(workers)
    print(listOfWorkers)
    print(hosts)
    listOfManager = [manager]
    trueIP = get_IP(manager)
    results = Host.ssh(hosts=hosts, command='sudo useradd slurm')
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command='sudo cp -R /usr/lib/pmix /clusterfs')
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command='sudo cp -R /clusterfs/pmix /usr/lib')
    print(Printer.write(results))
    results = Host.ssh(hosts=hosts, command='cd /usr/lib/pmix/source/ && sudo '
                                            './autogen.sh && cd ../build/2.1/ && sudo ../../source/configure '
                                            '--prefix=/usr/local && '
                                            'sudo make -j install >/dev/null')
    print(Printer.write(results))

    results = Host.ssh(hosts=manager, command='git clone https://github.com/SchedMD/slurm && cp -R slurm '
                                              '/clusterfs')
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command='sudo cp -R /clusterfs/slurm ~')
    print(Printer.write(results))
    results = Host.ssh(hosts=hosts, command='cd slurm && sudo ./configure --enable-debug --with-pmix '
                                            '--enable-deprecated --with-munge')
    print(Printer.write(results))
    results = Host.ssh(hosts=hosts, command='cd slurm && sudo make -j install > /dev/null')
    print(Printer.write(results))

    script = textwrap.dedent(
        f"""
        sudo curl -L https://raw.githubusercontent.com/cloudmesh/cloudmesh-mpi/main/doc/chapters/slurm/configs/slurm.conf > ~/slurm.conf
        sudo mv ~/slurm.conf /usr/local/etc/
        sudo sed -i 's/SlurmctldHost=workstation/SlurmctldHost={manager}({trueIP})/g' /usr/local/etc/slurm.conf
        sudo sed -i "$(( $(wc -l </usr/local/etc/slurm.conf)-2+1 )),$ d" /usr/local/etc/slurm.conf
        """)
    hostexecute(script, manager)
    results = Host.ssh(hosts=workers, command="cat /proc/sys/kernel/hostname")
    print(Printer.write(results))
    hostnames = []
    for entry in results:
        currentHostname = str(entry["stdout"])
        hostnames.append(currentHostname)
    print(hostnames)
    results = Host.ssh(hosts=workers, command="/sbin/ifconfig eth0 | grep 'inet' | cut -d: -f2")
    ipaddresses = []
    trueIPs = []
    print(Printer.write(results))
    for entry in results:
        currentIP = str(entry["stdout"])
        ipaddresses.append(currentIP)
    for x in ipaddresses:
        x2 = x.replace('inet ', '')
        x3 = x2.split(' ')
        print(x3)
        x4 = [y for y in x3 if y]
        print(x4)
        trueIP = x4[0]
        print(trueIP)
        trueIPs.append(trueIP)
    print(trueIPs)
    coreCounts = []
    results = Host.ssh(hosts=workers,
                       command="cat /sys/devices/system/cpu/cpu[0-9]*/topology/core_cpus_list | sort -u | wc -l")
    for entry in results:
        currentCoreCount = str(entry["stdout"])
        coreCounts.append(currentCoreCount)
    for x in range(len(hostnames)):
        command = f'echo "NodeName={hostnames[x]} NodeAddr={trueIPs[x]} CPUs={coreCounts[x]} State=UNKNOWN" '\
                  '| sudo tee /usr/local/etc/slurm.conf -a'
        results = Host.ssh(hosts=manager,
                           command=command)
        print(Printer.write(results))

    script = textwrap.dedent(
        f"""
        echo "PartitionName=mycluster Nodes={workers} Default=YES MaxTime=INFINITE State=UP" | sudo tee /usr/local/etc/slurm.conf -a
        sudo rm /clusterfs/slurm.conf
        sudo cp /usr/local/etc/slurm.conf /clusterfs
        sudo cp /etc/munge/munge.key /clusterfs
        sudo systemctl enable munge
        sudo systemctl start munge
        """)
    hostexecute(script, manager)
    results = Host.ssh(hosts=workers, command='sudo cp /clusterfs/slurm.conf /usr/local/etc/slurm.conf')
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command='sudo chown -R slurm:slurm /var/spool/')
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command='cd ~/slurm/etc/ && sudo cp slurmd.service /etc/systemd/system/')
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command='cd ~/slurm/etc/ && sudo cp slurmctld.service /etc/systemd/system/')
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command='sudo systemctl enable slurmd')
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command='sudo systemctl start slurmd')
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command='sudo systemctl enable slurmctld')
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command='sudo systemctl start slurmctld')
    print(Printer.write(results))
    results = Host.ssh(hosts=hosts, command="touch step4")
    print(Printer.write(results))
    StopWatch.stop("Current section time")
    StopWatch.benchmark()
    tell_user_rebooting()


# a = readfile("test1")
# writefile("test2",a)

# StopWatch.start("Total Runtime")

# Here begins the script aside from the function definitions. In this part we run the steps by calling functions.

banner("SLURM on Raspberry Pi Cluster Installation")

# executing reading of device names.

manager = managerNamer()

step0done = check_step(0, manager)
if not step0done:
    step0()

workers = read_user_input_workers(manager)

hosts = hostsVariable(manager, workers)

steps = [
    (1, step1),
    (2, step2),
    (3, step3),
    (4, step4)
]

for i, step in steps:
    if not check_step(i, hosts):
        banner(f"Step {i} is not done. Performing step {i} now.")
        step()


'''
#def parallel_execute(hosts,command):
#  os.system("cms host ssh "+hosts+" \"'"+command+""'\"")
#
#parallel_execute(hosts,"sudo apt-get update")
#for host in ehosts:
#  os.system("cms host ssh "+hosts+" 'touch step1'")
# print (names)
results4 = Host.ssh(hosts=hosts,
                   command="cat step1")
print(results4)
StopWatch.stop("Total Runtime")
StopWatch.benchmark()
'''

# </pre>
