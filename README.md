# my-cli-tool

A small, extensible command line tool written in Python.

## Requirements

- Python 3.8 or newer

## Install

```bash
git clone https://github.com/shenshilin-max/my-cli-tool.git
cd my-cli-tool
python -m pip install -e .
```

## Usage

```bash
my-cli-tool greet
my-cli-tool greet fpga --upper
my-cli-tool --version
```

The same commands work without installing, as long as `src` is on `PYTHONPATH`:

```bash
python -m my_cli_tool greet fpga
```

## Layout

```
my-cli-tool/
├── pyproject.toml            # packaging + console script entry point
├── src/my_cli_tool/
│   ├── __init__.py           # package version
│   ├── __main__.py           # python -m my_cli_tool
│   ├── cli.py                # argument parsing, dispatch
│   └── commands/
│       ├── __init__.py
│       └── greet.py          # a sample sub-command
└── tests/test_cli.py         # unittest suite
```

## Adding a command

1. Create `src/my_cli_tool/commands/<name>.py` with `add_parser(subparsers)` and
   `run(args) -> int`, following `greet.py`.
2. Register it in `cli.build_parser()`.
3. Add a test in `tests/`.

## Tests

```bash
python -m unittest discover -s tests
```

Run from the repository root with `src` on `PYTHONPATH`, for example:

```bash
# Windows (PowerShell)
$env:PYTHONPATH = "src"; python -m unittest discover -s tests

# Linux / macOS
PYTHONPATH=src python -m unittest discover -s tests
```

## License

Not specified yet.
