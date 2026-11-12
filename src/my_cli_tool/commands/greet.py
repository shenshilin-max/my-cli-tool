"""``my-cli-tool greet`` -- sample sub-command.

Copy this file to add a new command: register the parser in ``add_parser`` and
implement the behaviour in ``run``.
"""

from __future__ import annotations

import argparse


def add_parser(subparsers: argparse._SubParsersAction) -> argparse.ArgumentParser:
    parser = subparsers.add_parser(
        "greet",
        help="Print a greeting",
        description="Print a greeting for the given name.",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="world",
        help="who to greet (default: world)",
    )
    parser.add_argument(
        "--upper",
        action="store_true",
        help="print the greeting in upper case",
    )
    return parser


def run(args: argparse.Namespace) -> int:
    text = "Hello, {}!".format(args.name)
    print(text.upper() if args.upper else text)
    return 0
