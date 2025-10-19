#!/usr/bin/env -S python3 -OO
# -*- coding: utf-8 -*-

# ### # Imports

import sys, os
from enum import IntEnum

import argparse

# ### # Global Variables

VERBOSE: bool = False

class MAKE_DIRS_RET(IntEnum):
	SUCCESS = 0
	ALREADY_EXISTS = 1
	OS_ERROR = 2

# ## # Helper Functions

def print_verbose(message: str) -> None:
	"""Prints a message if verbose mode is enabled."""

	if VERBOSE: # Only print if VERBOSE is True from arguments
		print(message, file=sys.stderr)

def make_dirs(path: str) -> MAKE_DIRS_RET:
	"""Creates directories recursively, similar to `mkdir -p`."""

	try:
		os.makedirs(path) # Create directories recursively
		print_verbose(f"Created directories for path: {path}")
	except FileExistsError as e: # If directories already exist
		print_verbose(f"Directories already exist for path: {path} - {e}")
		return MAKE_DIRS_RET.ALREADY_EXISTS
	except OSError as e: # Other OS-related errors
		print_verbose(f"Error creating directories for path: {path} - {e}")
		return MAKE_DIRS_RET.OS_ERROR

	return MAKE_DIRS_RET.SUCCESS

# ### # Main Function

def main(argv: list[str], argc: int) -> int:
	# Parse arguments
	parser = argparse.ArgumentParser(prog=argv[0], description="Local Package Installer: A script for assigning what's in a directory to their `/usr/local` directories.", epilog="Example usage: local-package-installer /path/to/directory") # Parser setup
	parser.add_argument("directory", type=str, help="The directory to install packages from.") # Target
	parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.") # Optional flag for verbosity
	args = parser.parse_args(argv[1:])

	# Set global verbosity flag
	global VERBOSE
	VERBOSE = args.verbose

	# TODO: Loop over each directory in the chosen directory and copy the files to their respective `/usr/local` locations.
	print_verbose(f"Installing packages from directory: {args.directory}")

	return 0

# ### #

if __name__ == "__main__":
	sys.exit(main(sys.argv, len(sys.argv)))
