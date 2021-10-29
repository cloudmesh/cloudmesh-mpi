#!/usr/bin/env python

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import banner
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.Host import Host
from cloudmesh.common.util import readfile,writefile
from cloudmesh.common.Printer import Printer
from pprint import pprint
import os
import sys

def step1(results):
    banner("Step 1")
    print(Printer.write(results,header=["host","stderr"]))

    #results = Host.ssh(hosts=hosts, command="sudo apt-get update")
    #pprint(results)
    # parallel_execute(hosts,"sudo apt install ntpdate -y")
    #results2 = Host.ssh(hosts=hosts, command="sudo apt install ntpdate -y")
    #pprint(results2)

    #results3 = Host.ssh(hosts=hosts, command="touch step1")
    #print(results3)
    #results4 = Host.ssh(hosts=hosts, command="sudo reboot")
    #pprint(results4)
    # results4 = Host.ssh(hosts=hosts,command="sudo shutdown -r now")


def step2():
    banner("Step 2")
    results = Host.ssh(hosts=hosts, command="ls")
    pprint(results)


#a = readfile("test1")
#writefile("test2",a)

#StopWatch.start("Total Runtime")
hosts = "red,red0[1-3]"
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
    pprint(results)
    step2()
else:
    step1(results)


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