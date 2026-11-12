"""Command line entry point.

Sub-commands live in :mod:`my_cli_tool.commands`; each module registers its own
parser and returns an int exit code from its ``run`` function.
"""

from __future__ import annotations

import argparse
from typing import Optional, Sequence

from . import __version__
from .commands import greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="my-cli-tool",
        description="A small, extensible command line tool.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="my-cli-tool {}".format(__version__),
    )

    subparsers = parser.add_subparsers(dest="command", metavar="<command>")
    subparsers.required = True

    greet.add_parser(subparsers)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "greet":
        return greet.run(args)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
