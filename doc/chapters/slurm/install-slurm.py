#!/usr/bin/env python

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import banner
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.Host import Host
from cloudmesh.common.util import readfile,writefile
from cloudmesh.common.Printer import Printer
from cloudmesh.common.console import Console
from cloudmesh.common.util import yn_choice
from pprint import pprint
import os
import sys
import re
from cloudmesh.burn.usb import USB
from cloudmesh.burn.sdcard import SDCard

hosts = "red,red0[1-3]"
workers = "red0[1-3]"
manager = "red"

def step0():
    banner("Welcome to Slurm Installation. Initializing preliminary steps.")
    print("We assume that your manager and workers follow the 'red' naming schema.")
    user_input_workers = input(str('''Please enter the naming schema of your red workers. For example, if you have 3\n
    workers then enter "red0[1-3]". Another example for 7 workers is "red0[1-7]". Do not include quotation marks\n'''))
    results = Host.ssh(hosts=manager, command="touch user_input_workers")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command=f'''echo '{user_input_workers}' >> user_input_workers''')
    print(Printer.write(results))

    # intro and asking for workers from user
    results = Host.ssh(hosts=manager, command='cat user_input_workers')
    print(Printer.write(results))
    for entry in results:
        print(str(entry["stdout"]))
        workers = str(entry["stdout"])

    # formulating hosts variable which has manager AND workers
    hosts = f'''{manager},{workers}'''
    hosts = str(hosts)
    print(hosts)
    results3 = Host.ssh(hosts=hosts, command="touch step0")
    print(Printer.write(results3))

def step1(results):
    # intro and asking for workers from user
    banner("Initializing Step 1 now.")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command='cat user_input_workers')
    print(Printer.write(results))
    for entry in results:
        print(str(entry["stdout"]))
        workers = str(entry["stdout"])

    # formulating hosts variable which has manager AND workers
    hosts = f'''{manager},{workers}'''
    hosts = str(hosts)
    print(hosts)

    results = Host.ssh(hosts=hosts, command="sudo apt-get update")
    print(Printer.write(results))
    #parallel_execute(hosts,"sudo apt install ntpdate -y")
    results2 = Host.ssh(hosts=hosts, command="sudo apt install ntpdate -y")
    print(Printer.write(results2))

    results3 = Host.ssh(hosts=hosts, command="touch step1")
    print(Printer.write(results3))
    print("cms host reboot "+hosts)
    os.system("cms host reboot "+hosts)
    #results4 = Host.ssh(hosts=hosts,command="sudo shutdown -r now")


def step2():
    banner("Step 2")
    if not yn_choice('Please insert USB storage medium into top USB 3.0 (blue) port on manager pi and press y when done'):
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
    results = Host.ssh(hosts=manager, command='cat user_input_workers')
    print(Printer.write(results))
    for entry in results:
        print(str(entry["stdout"]))
        workers = str(entry["stdout"])

    # formulating hosts variable which has manager AND workers
    hosts = f'''{manager},{workers}'''
    hosts = str(hosts)
    print(hosts)

    card = SDCard()
    card.info()
    USB.check_for_readers()
    print('Please enter the device path e.g. "/dev/sda" or no input default to /dev/sda (remember, do not add quotation marks):')
    device = input()
    if device == '':
        device = '/dev/sda'
    print(device)
    print(f"sudo mkfs.ext4 {device}")
    results = Host.ssh(hosts=manager, command=f"sudo mkfs.ext4 {device}")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo mkdir /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo chown nobody.nogroup -R /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo chmod 777 -R /clusterfs")
    print(Printer.write(results))
    print(os.system(f"sudo blkid {device}"))
    results9 = Host.ssh(hosts=manager, command=f"sudo blkid {device}")
    print(Printer.write(results9))
    for entry in results9:
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
    results = Host.ssh(hosts=manager, command=f'''echo "UUID={result2} /clusterfs ext4 defaults 0 2" | sudo tee /etc/fstab -a''')
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo mount -a")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo chown nobody.nogroup -R /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo chmod -R 766 /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo apt install nfs-kernel-server -y")
    print(Printer.write(results))
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
    results = Host.ssh(hosts=manager, command=f'''echo "/clusterfs {trueIP}/24(rw,sync,no_root_squash,no_subtree_check)" | sudo tee /etc/exports -a''')
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo exportfs -a")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo apt install nfs-common -y")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo mkdir /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo chown nobody.nogroup /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo chmod -R 777 /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command=f'''echo "{trueIP}:/clusterfs    /clusterfs    nfs    defaults   0 0" | sudo tee /etc/fstab -a''')
    print(Printer.write(results))
    results3 = Host.ssh(hosts=hosts, command="touch step2")
    print(Printer.write(results3))
    print("cms host reboot "+hosts)
    os.system("cms host reboot "+hosts)


def step3():
    #getting ip in case step 2 has not run
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

    # executing reading of workers
    results = Host.ssh(hosts=manager, command='cat user_input_workers')
    print(Printer.write(results))
    for entry in results:
        print(str(entry["stdout"]))
        workers = str(entry["stdout"])

    # formulating hosts variable which has manager AND workers
    hosts = f'''{manager},{workers}'''
    hosts = str(hosts)
    print(hosts)

    #now doing actual step 3
    results = Host.ssh(hosts=manager, command="sudo systemctl status nfs-server.service")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo systemctl start nfs-server.service")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo mount -a")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo apt install slurm-wlm -y")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo cp /usr/share/doc/slurm-client/examples/slurm.conf.simple.gz /etc/slurm-llnl")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo gzip -d /etc/slurm-llnl/slurm.conf.simple.gz")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo mv /etc/slurm-llnl/slurm.conf.simple /etc/slurm-llnl/slurm.conf")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command=f'''sudo sed -i 's/SlurmctldHost=workstation/SlurmctldHost={manager}({trueIP})/g' /etc/slurm-llnl/slurm.conf''')
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command=f'''sudo sed -i "$(( $(wc -l </etc/slurm-llnl/slurm.conf)-2+1 )),$ d" /etc/slurm-llnl/slurm.conf''')
    print(Printer.write(results))
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
    results = Host.ssh(hosts=workers, command="cat /sys/devices/system/cpu/cpu[0-9]*/topology/core_cpus_list | sort -u | wc -l")
    for entry in results:
        currentCoreCount = str(entry["stdout"])
        coreCounts.append(currentCoreCount)
    for x in range(len(hostnames)):
        results = Host.ssh(hosts=manager,
                           command=f'''echo "NodeName={hostnames[x]} NodeAddr={trueIPs[x]} CPUs={coreCounts[x]} State=UNKNOWN" | sudo tee /etc/slurm-llnl/slurm.conf -a''')
        print(Printer.write(results))
    results = Host.ssh(hosts=manager, command=f'''echo "PartitionName=mycluster Nodes={workers} Default=YES MaxTime=INFINITE State=UP" | sudo tee /etc/slurm-llnl/slurm.conf -a''')
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo curl -L https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/chapters/slurm/cgroup.conf > ~/cgroup.conf")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo curl -L https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/chapters/slurm/cgroup_allowed_devices_file.conf > ~/cgroup_allowed_devices_file.conf")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo cp ~/cgroup.conf /etc/slurm-llnl/cgroup.conf")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo cp ~/cgroup_allowed_devices_file.conf /etc/slurm-llnl/cgroup_allowed_devices_file.conf")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo rm ~/cgroup.conf")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo rm ~/cgroup_allowed_devices_file.conf")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo cp /etc/slurm-llnl/slurm.conf /etc/slurm-llnl/cgroup.conf /etc/slurm-llnl/cgroup_allowed_devices_file.conf /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo cp /etc/munge/munge.key /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo systemctl enable munge")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo systemctl start munge")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo systemctl enable slurmctld")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sudo systemctl start slurmctld")
    print(Printer.write(results))
    results3 = Host.ssh(hosts=hosts, command="touch step3")
    print(Printer.write(results3))
    print("cms host reboot "+hosts)
    os.system("cms host reboot "+hosts)


def step4():
    # executing reading of workers
    results = Host.ssh(hosts=manager, command='cat user_input_workers')
    print(Printer.write(results))
    for entry in results:
        print(str(entry["stdout"]))
        workers = str(entry["stdout"])

    # formulating hosts variable which has manager AND workers
    hosts = f'''{manager},{workers}'''
    hosts = str(hosts)
    print(hosts)

    #getting hostname count
    results = Host.ssh(hosts=workers, command="cat /proc/sys/kernel/hostname")
    print(Printer.write(results))
    hostnames = []
    for entry in results:
        currentHostname = str(entry["stdout"])
        hostnames.append(currentHostname)
    print(hostnames)

    results = Host.ssh(hosts=workers, command="sudo chown nobody.nogroup /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo chmod -R 777 /clusterfs")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo apt install slurmd slurm-client -y")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo cp /clusterfs/munge.key /etc/munge/munge.key")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo cp /clusterfs/slurm.conf /etc/slurm-llnl/slurm.conf")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo cp /clusterfs/cgroup* /etc/slurm-llnl")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo systemctl enable munge")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo systemctl start munge")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo systemctl enable slurmd")
    print(Printer.write(results))
    results = Host.ssh(hosts=workers, command="sudo systemctl start slurmd")
    print(Printer.write(results))
    results = Host.ssh(hosts=manager, command="sinfo")
    print(Printer.write(results))
    banner("Slurm installed")
    results3 = Host.ssh(hosts=hosts, command="touch step4")
    print(Printer.write(results3))
    print("Rebooting cluster now.")
    banner("After successful reboot, test slurm by issuing $ srun --nodes=3 hostname (change 3 to number of nodes if necessary)")
    os.system("cms host reboot "+hosts)


#a = readfile("test1")
#writefile("test2",a)

#StopWatch.start("Total Runtime")

banner("Slurm on Raspberry Pi Cluster Installation")
results9001 = Host.ssh(hosts=manager, command="ls step0")
print(Printer.write(results9001))
step0done = True
for entry in results9001:
    if 'step0' in str(entry["stdout"]) and 'cannot access' in str(entry["stdout"]):
        step0done = False
        entry["stderr"] = "False"

if not step0done:
    step0()

# executing reading of workers
results = Host.ssh(hosts=manager, command='cat user_input_workers')
print(Printer.write(results))
for entry in results:
    print(str(entry["stdout"]))
    workers = str(entry["stdout"])

# formulating hosts variable which has manager AND workers
hosts = f'''{manager}'''+f''',{workers}'''
hosts = str(hosts)
print(hosts)

results = Host.ssh(hosts=hosts,command="ls step1")

completed = True
for entry in results:
    if 'step1' in str(entry["stderr"]) and 'cannot access' in str(entry["stderr"]):
        completed = False
        entry["stderr"] = "False"
if completed:
    banner("Step 1 is done.")
    pprint(results)
    results42 = Host.ssh(hosts=hosts, command="ls step2")
    completedSecondStep = True
    for entry in results42:
        if 'step2' in str(entry["stderr"]) and 'cannot access' in str(entry["stderr"]):
            completedSecondStep = False
            entry["stderr"] = "False"
    if completedSecondStep:
        banner("Step 2 is done.")
    if not completedSecondStep:
        banner("Step 2 is not done. Performing Step 2 now.")
        step2()
if not completed:
    banner("Step 1 is not done. Performing step 1 now.")
    step1(results)
    #os.system('touch step1')


results42 = Host.ssh(hosts=hosts,command="ls step2")
completed2 = True
for entry in results42:
    if 'step2' in str(entry["stderr"]) and 'cannot access' in str(entry["stderr"]):
        completed2 = False
        entry["stderr"]="False"
if completed2:
    banner("Step 2 is done.")
    pprint(results42)
    results43 = Host.ssh(hosts=hosts, command="ls step3")
    completedThirdStep = True
    for entry in results43:
        if 'step3' in str(entry["stderr"]) and 'cannot access' in str(entry["stderr"]):
            completedThirdStep = False
            entry["stderr"] = "False"
    if not completedThirdStep:
        banner("Step 3 is not done. Performing step 3")
        step3()
if not completed2:
    banner("Step 2 is not done. Performing step 2 now.")
    step2()
    #os.system('touch step2')

results50 = Host.ssh(hosts=hosts,command="ls step3")
completedThirdStep = True
for entry in results50:
    if 'step3' in str(entry["stderr"]) and 'cannot access' in str(entry["stderr"]):
        completedThirdStep = False
        entry["stderr"]="False"
if completedThirdStep:
    banner("Third step is done")
if not completedThirdStep:
    banner("Third step is not done. Executing third step now")
    step3()

results51 = Host.ssh(hosts=hosts,command="ls step4")
completedFourthStep = True
for entry in results51:
    if 'step4' in str(entry["stderr"]) and 'cannot access' in str(entry["stderr"]):
        completedFourthStep = False
        entry["stderr"]="False"
if completedFourthStep:
    banner("Fourth step is done so slurm should already be installed")
if not completedFourthStep:
    banner("Fourth step is not done. Executing fourth step now")
    step4()



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
