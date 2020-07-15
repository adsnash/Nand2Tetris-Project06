#!/usr/bin/env python3

import argparse
from assembler import Assembler


parser = argparse.ArgumentParser(
	prog="main.py",
	description="Convert a .asm file into .hack assembly file",
)

parser.add_argument("asm_path", help="Path to .asm file to convert", type=str)

parser.add_argument(
	"--debug",
	"--d",
	action="store_true",
	default=False,
	help="Whether to print steps/timing (True) or not (False) DEFAULT: False",
	dest="debug",
)

__doc__ = "\n" + parser.format_help()


def main():
	args = parser.parse_args()
	a = Assembler(args.debug)
	a.assemble(args.asm_path)


if __name__ == "__main__":
	main()

