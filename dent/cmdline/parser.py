"""
Commandline parser
"""

import argparse
import logging

log = logging.getLogger('talque.app')


description = """
inDENT commandline interface
"""
 

def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--log', dest='log', default=None,
                        help='one of [DEBUG, INFO, ERROR, WARNING, CRITICAL]')

    subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')
    
    tree = subparsers.add_parser('tree', help='visualize tree')
    tree.add_argument('filename', type=str, help='Source file to analyze')

    return parser
