from __future__ import print_function

import sys

from anilius.cli.anilius import cli


def main(as_module=False):
    cli.main(args=sys.argv[1:], prog_name="python -m anilius" if as_module else None)


if __name__ == "__main__":
    main(as_module=True)
