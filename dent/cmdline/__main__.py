import sys

from dent.cmdline.main import dent_main

if __name__ == '__main__':
    print(sys.argv)
    dent_main(sys.argv[1:])
