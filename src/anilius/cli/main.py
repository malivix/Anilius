import os
import sys

sys.path.append(os.getcwd())


def main(as_module=False):
    from anilius.cli.anilius import cli

    cli.main(args=sys.argv[1:], prog_name="python -m anilius" if as_module else None)


if __name__ == "__main__":
    main(as_module=True)
