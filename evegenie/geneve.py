#!/usr/bin/env python
"""
Tool for generating Eve schemas from JSON.
"""
from __future__ import print_function
import os.path
import sys
from docopt import docopt
from evegenie import EveGenie
from cloudmesh.common.error import Error

def run(filename):
    """
    Create an instance of EveGenie from a json file. Then write it to file.

    :param filename: input filename
    :return:
    """
    print ('Converting: {}'.format(filename))
    outfile = '{}.settings.py'.format(filename.split('.', 1)[0])
    # print ('Output:', outfile)

    eg = EveGenie(filename=filename)

    eg.write_file(outfile)
    print ('Settings file written to {}'.format(outfile))


def main():
    """evegenie.

    Usage:
      evegenie --help
      evegenie FILENAME

    Arguments:
      FILENAME  The filename containing the schema

    Options:
       -h --help

    Description:
      Creates a schema from objects defined in a jason file
    """

    arguments = docopt(main.__doc__, sys.argv[1:])

    # print(arguments)

    if arguments["--help"]:
        print(main.__doc__)
        sys.exit()
    try:
        filename = arguments["FILENAME"]

        if os.path.isfile(filename):
            run(filename)
    except Exception as e:
        print ("ERROR: generating schema")
        Error.traceback(error=e, debug=True, trace=True)


if __name__ == '__main__':
    main()
