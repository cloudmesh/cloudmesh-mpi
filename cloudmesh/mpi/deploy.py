from cloudmesh.common.JobSet import JobSet
from cloudmesh.common.Printer import Printer
from cloudmesh.common.console import Console


class Deploy:

    def __init__(self, hosts, users):
        self.hosts = hosts
        self.users = users
        #if len(users == 1):
        #    for i in range (0, len(hosts)):
        #        users[i] = users[0]

    def _print_JobSet(self, jobSet, stdout=False):
        d = dict(jobSet.job)
        for key in jobSet.job:
            if isinstance(jobSet.job[key]["stdout"], bytes):
                jobSet.job[key]["stdout"] = jobSet.job[key]["stdout"].decode("utf-8")
            if isinstance(jobSet.job[key]["stderr"], bytes):
                jobSet.job[key]["stderr"] = jobSet.job[key]["stderr"].decode("utf-8")

        if stdout:
            print(Printer.write(d,
                                order=['host', 'returncode', 'stderr', 'stdout'],
                                output='table'))
        else:
            print(Printer.write(d,
                                order=['host', 'returncode', 'stderr'],
                                output='table'))

    def jobset_test(self):
        Console.info("Testing jobSet")
        jobSet = JobSet("ls", executor=JobSet.ssh)
        for host in self.hosts:
            jobSet.add_directory({"name": host, "host": host, "command": "sudo ls -al /; ls -al /home/root"})
        jobSet.run()
        self._print_JobSet(jobSet)

    def install_mpi_raspberry(self):
        Console.info("Installing mpi on hosts")
        Console.info("sudo apt-get install openmpi-bin -y; source ~/ENV3/bin/activate; pip3 install mpi4py")
        Console.info("This may take several minutes")
        jobSet = JobSet("install mpi", executor=JobSet.ssh)
        for host in self.hosts:
            jobSet.add_directory({"name": host, "host": host, "command": "sudo apt-get install openmpi-bin -y; source ~/ENV3/bin/activate; pip3 install mpi4py"})
        jobSet.run()
        d = dict(jobSet.job)
        self._print_JobSet(jobSet)

    def install_mpi_ubuntu(self):
        Console.info("Installing mpi on hosts")
        Console.info("sudo apt-get install mpich-doc mpich -y; source ~/ENV3/bin/activate; pip3 install mpi4py")
        Console.info("This may take several minutes")
        jobSet = JobSet("install mpi", executor=JobSet.ssh)
        for host in self.hosts:
            jobSet.add_directory({"name": host, "host": host, "command": "sudo apt-get install mpich-doc mpich -y; source ~/ENV3/bin/activate; pip3 install mpi4py"})
        jobSet.run()
        d = dict(jobSet.job)
        self._print_JobSet(jobSet)

    def version_raspberry(self):
        Console.info("Checking version of mpi on hosts")
        Console.info("mpicc --showme:version")
        jobSet = JobSet("mpi version", executor=JobSet.ssh)
        for host in self.hosts:
            jobSet.add_directory({"name": host, "host": host, "command": "mpicc --showme:version"})
        jobSet.run()
        self._print_JobSet(jobSet, stdout=True)

    def version_ubuntu(self):
        Console.info("Checking version of mpi on hosts")
        Console.info("mpicc --showme:version")
        jobSet = JobSet("mpi version", executor=JobSet.ssh)
        for host in self.hosts:
            jobSet.add_directory({"name": host, "host": host, "command": "mpichversion | head  -n 1"})
        jobSet.run()
        self._print_JobSet(jobSet, stdout=True)

    def install_python_dev_env(self):
        Console.info("Installing essential python packages")
        Console.info("sudo apt-get install python3-venv python3-wheel python3-dev build-essential python3-pip -y; pip3 install pip -U; python3 -m venv ~/ENV3")
        Console.info("This may take several minutes")
        bashrc = "source ${HOME}/ENV3/bin/activate"
        jobSet = JobSet("python install", executor=JobSet.ssh)
        for host in self.hosts:
            jobSet.add_directory({"name": host, "host": host,
                        "command": "sudo apt-get install python3-venv python3-wheel python3-dev build-essential python3-pip -y; pip3 install pip -U; python3 -m venv ~/ENV3 ; "
                       f'grep -qF -- "{bashrc}" ~/.bashrc || echo "{bashrc}" >> "${{HOME}}/.bashrc"'})
        jobSet.run()
        self._print_JobSet(jobSet)

    def uninstall_mpi_raspberry(self):
        Console.info("Uninstalling mpi on hosts")
        Console.info("sudo apt-get --purge remove openmpi-bin -y; source ~/ENV3/bin/activate; pip3 uninstall mpi4py -y")
        jobSet = JobSet("uninstall mpi", executor=JobSet.ssh)
        for host in self.hosts:
            jobSet.add_directory({"name": host, "host": host,
                        "command": "sudo apt-get --purge remove openmpi-bin -y; source ~/ENV3/bin/activate; pip3 uninstall mpi4py -y"})
        jobSet.run()
        d = dict(jobSet.job)
        self._print_JobSet(jobSet,stdout=True)

    def uninstall_mpi_ubuntu(self):
        Console.info("Uninstalling mpi on hosts")
        Console.info("sudo apt-get --purge remove mpich-doc mpich -y; source ~/ENV3/bin/activate; pip3 uninstall mpi4py -y")
        jobSet = JobSet("uninstall mpi", executor=JobSet.ssh)
        for host in self.hosts:
            jobSet.add_directory({"name": host, "host": host,
                        "command": "sudo apt-get --purge remove mpich-doc mpich -y; source ~/ENV3/bin/activate; pip3 uninstall mpi4py -y"})
        jobSet.run()
        d = dict(jobSet.job)
        self._print_JobSet(jobSet,stdout=True)
