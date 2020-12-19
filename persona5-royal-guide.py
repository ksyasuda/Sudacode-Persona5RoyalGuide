#!/usr/bin/env python3

from P5RGuide.Utility.utility import get_opts
from P5RGuide.Utility.utility import handle_options

def main():
    """The literal main"""
    options, remainder, argc, argv = get_opts()
    handle_options(options, remainder, argc, argv)

if __name__ == '__main__':
    main()
