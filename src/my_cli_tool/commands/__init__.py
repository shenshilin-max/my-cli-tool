"""Sub-commands of my-cli-tool.

Each module exposes ``add_parser(subparsers)`` and ``run(args) -> int`` so a new
command only has to be one new file plus one line in ``cli.build_parser``.
"""

from . import greet

__all__ = ["greet"]
