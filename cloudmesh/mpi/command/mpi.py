from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.mpi.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.parameter import Parameter

class MpiCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_mpi(self, args, arguments):
        """
        ::

          Usage:
                mpi deploy HOSTS

          This command deploys HOSTS mpi. At this time this command is 
          intended only to be used with Raspberry PIs

          Arguments:
              HOSTS   parameterized list of hosts

        """
        arguments.hosts = arguments['HOSTS']

        VERBOSE(arguments)

        if arguments.deploy:

            banner("Install MPI on hosts")

            print (arguments.hosts)

            raise NotImplementedError

            
        return ""
