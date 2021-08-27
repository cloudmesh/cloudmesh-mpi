from cloudmesh.common.Shell import Shell

#
# It would be best to use our parallel job command.
# I just wrote this down here so we have a start and can test the sudo
#

class Deploy:
    """
    Installs mpi on the specified host
    """
    
    def __init__(host: str, user:str):
        self.host = host
        self.user = user

    def _ssh(command):
        r = Shell.ssh("{self.user}@{self.host} {command}")
        return r
    
    def mpi():
        # can we do this? e.g. passwd?
        r = _ssh("sudo apt-get install openmpi-bin")
        r = _ssh("pip install mpi4py")

    def version():
         r = _ssh("mpicc --showme:version")
         return r

class DeployOnCluster:

    def __init__(hosts, users):
        self.hosts = hosts
        self.users = users
        if len(users == 1):
            for i in range (0, len(hosts)):
                users[i] = users[0]

    def mpi():
        for i in range(0, len(hosts)):
            host = hosts[i]
            user = users[i]
            deploy = Deploy(host, user)
            deploy.mpi()
