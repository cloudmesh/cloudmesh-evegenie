#!/usr/bin/env python
"""
Tool for generating Eve schemas from JSON.
"""

import os.path
import sys
from docopt import docopt
from evegenie import EveGenie


def run(filename):
    """
    Create an instance of EveGenie from a json file. Then write it to file.

    :param filename: input filename
    :return:
    """
    print ('converting contents of {}'.format(filename))
    outfile = '{}.settings.py'.format(filename.split('.', 1)[0])
    print ('file:', outfile)

    eg = EveGenie(filename=filename)

    print ("OOO", eg)

    eg.write_file(outfile)
    print ('settings file written to {}'.format(outfile))


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

    print(arguments)

    if arguments["--help"]:
        print(main.__doc__)
        sys.exit()
    try:
        filename = arguments["FILENAME"]

        if os.path.isfile(filename):
            run(filename)
    except Exception as e:
        print ("ERROR: generating schema")
        print (e)


if __name__ == '__main__':
    main()
