#!/usr/bin/env python

from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.util import banner
from cloudmesh.common.Parameter import Parameter
from cloudmesh.common.util import readfile,writefile
import os

#a = readfile("test1")
#writefile("test2",a)

StopWatch.start("Total Runtime")
hosts = "red,red0[1-3]"
ehosts = Parameter.expand(hosts)

cloudmesh.banner("Slurm on Raspberry Pi Cluster Installation")
results4 = Host.ssh(hosts=hosts,command="ls step1")
print(results4)
exit
#def parallel_execute(hosts,command):
#  os.system("cms host ssh "+hosts+" \"'"+command+""'\"")
#
#parallel_execute(hosts,"sudo apt-get update")
results = Host.ssh(hosts=hosts,command="sudo apt-get update")
print(results)
#parallel_execute(hosts,"sudo apt install ntpdate -y")
results2 = Host.ssh(hosts=hosts,command="sudo apt install ntpdate -y")
print(results2)

results3 = Host.ssh(hosts=hosts,command="sudo reboot")
print(results3)
# results3 = Host.ssh(hosts=hosts,command="sudo shutdown -r now")

#for host in ehosts:
#  os.system("cms host ssh "+hosts+" 'touch step1'")

results3 = Host.ssh(hosts=hosts,command="touch step1")
print(results3)
# print (names)

results4 = Host.ssh(hosts=hosts,
                   command="cat step1")
print(results4)


StopWatch.stop("Total Runtime")
StopWatch.benchmark()
