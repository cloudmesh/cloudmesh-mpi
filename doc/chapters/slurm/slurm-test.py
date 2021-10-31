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

hosts = "red,red0[1-3]"

def step1(results):
    banner("Step 1")
    print(Printer.write(results))

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
    if not yn_choice('Please insert USB storage medium into top USB 3.0 (blue) port on manager pi red and press y when done'):
        Console.error("Terminating: User Break")
        return ""
    os.system('lsblk')
    if not yn_choice('Please confirm that sda1 is your USB which will be formatted by pressing y'):
        Console.error("Terminating: User Break")
        return ""
    


#a = readfile("test1")
#writefile("test2",a)

#StopWatch.start("Total Runtime")

ehosts = Parameter.expand(hosts)

banner("Slurm on Raspberry Pi Cluster Installation")
print(hosts)
print(ehosts)
results = Host.ssh(hosts=hosts,command="ls step1")

completed = True
for entry in results:
    if 'step1' in str(entry["stderr"]) and 'cannot access' in str(entry["stderr"]):
        completed = False
        entry["stderr"]="False"
if completed:
    banner("Step 1 is done. Executing step 2 now")
    pprint(results)
    step2()
else:
    banner("Step 1 is not done. Executing step 1 now")
    step1(results)
    #os.system('touch step1')


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
