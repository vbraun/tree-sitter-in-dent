import logging
from typing import Sequence

from dent.cmdline.cmdline_tree import dent_cmdline_tree
from dent.cmdline.parser import make_parser

logging.basicConfig()
log = logging.getLogger('tq_app')



def dent_main(commandline_args: Sequence[str]) -> None:
    parser = make_parser()
    args = parser.parse_args(commandline_args)
    print(args)
    if args.log is not None:
        level = getattr(logging, args.log)
        log.setLevel(level=level)
    if args.subcommand == 'tree':
        dent_cmdline_tree(args.filename)
