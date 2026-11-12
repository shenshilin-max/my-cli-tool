"""Tests for the command line interface."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from my_cli_tool.cli import main


class GreetTest(unittest.TestCase):
    def _run(self, argv):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = main(argv)
        return code, buffer.getvalue().strip()

    def test_default_name(self):
        code, output = self._run(["greet"])
        self.assertEqual(code, 0)
        self.assertEqual(output, "Hello, world!")

    def test_explicit_name(self):
        code, output = self._run(["greet", "fpga"])
        self.assertEqual(code, 0)
        self.assertEqual(output, "Hello, fpga!")

    def test_upper_flag(self):
        code, output = self._run(["greet", "fpga", "--upper"])
        self.assertEqual(code, 0)
        self.assertEqual(output, "HELLO, FPGA!")


if __name__ == "__main__":
    unittest.main()
