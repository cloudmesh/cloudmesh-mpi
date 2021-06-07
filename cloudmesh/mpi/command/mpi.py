from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.mpi.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE


class MpiCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_mpi(self, args, arguments):
        """
        ::

          Usage:
                mpi --file=FILE
                mpi list
                mpi cooper --file=FILE

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        arguments.FILE = arguments['--file'] or None

        VERBOSE(arguments)

        m = Manager()
        if arguments.cooper:
            print(arguments.FILE)
            print('hello cooper')
        elif arguments.FILE:
            print("option a")
            m.list(path_expand(arguments.FILE))

        elif arguments.list:
            print("option b")
            m.list("just calling list without parameter")
    #random comment
        #Console.error("This is just a sample")
        return ""
