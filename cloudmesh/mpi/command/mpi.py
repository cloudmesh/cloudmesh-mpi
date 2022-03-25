from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import banner
from cloudmesh.mpi.deploy import Deploy
from cloudmesh.common.parameter import Parameter


class MpiCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_mpi(self, args, arguments):
        """
        ::

          Usage:
                mpi deploy raspberry HOSTS
                mpi deploy ubuntu HOSTS
                mpi uninstall raspberry HOSTS
                mpi uninstall ubuntu HOSTS

          This command is used to install MPI on a cluster running Raspberry Pi OS or Ubuntu OS.

          Arguments:
              HOSTS   parameterized list of hosts

          Description:
              mpi deploy raspberry HOSTS

                  Will deploy mpi for raspberry OS HOSTS in a parallel manner and return installation results.

              mpi deploy ubuntu HOSTS

                  Will deploy mpi for ubuntu OS HOSTS (possibly running on raspberry pi platform) in a parallel manner
                  and return installation results.

              mpi uninstall raspberry HOSTS

                  Will uninstall mpi packagess from raspberry OS HOSTS.

              mpi uninstall ubuntu HOSTS

                  Will uninstall mpi packages from ubuntu OS HOSTS.

        """
        arguments.hosts = arguments['HOSTS']

        VERBOSE(arguments)

        if arguments.deploy and arguments.raspberry:

            banner("Install MPI on hosts")
            hosts = Parameter.expand(arguments.hosts)
            deploy = Deploy(hosts, ["pi"])
            deploy.install_python_dev_env()
            deploy.install_mpi_raspberry()
            deploy.version_raspberry()

        elif arguments.deploy and arguments.ubuntu:
            banner("Install MPI on hosts")
            hosts = Parameter.expand(arguments.hosts)
            deploy = Deploy(hosts, ["pi"])
            deploy.install_python_dev_env()
            deploy.install_mpi_ubuntu()
            deploy.version_ubuntu()

        elif arguments.uninstall and arguments.raspberry:
            banner("Uninstall MPI on hosts")
            hosts = Parameter.expand(arguments.hosts)
            deploy = Deploy(hosts, ["pi"])
            deploy.uninstall_mpi_raspberry()

        elif arguments.uninstall and arguments.ubuntu:
            banner("Uninstall MPI on hosts")
            hosts = Parameter.expand(arguments.hosts)
            deploy = Deploy(hosts, ["pi"])
            deploy.uninstall_mpi_ubuntu()

        return ""
