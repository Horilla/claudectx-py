"""
claudectx-py — Python wrapper for the claudectx CLI.

Delegates all commands to the `claudectx` npm package.
Install the npm package first: npm install -g claudectx
Or install via Homebrew: brew install Horilla/claudectx/claudectx
"""
from __future__ import annotations

import shutil
import subprocess
import sys

__version__ = "1.1.4"

NPM_PACKAGE = "claudectx"
NPM_VERSION = "1.1.4"

_INSTALL_HINT = (
    "\nclaudectx is not installed. Install it with:\n"
    "  npm install -g claudectx\n"
    "  # or via Homebrew:\n"
    "  brew tap Horilla/claudectx && brew install claudectx\n"
)


def _find_binary() -> str | None:
    """Return the path to the claudectx binary, or None if not found."""
    return shutil.which("claudectx")


def _ensure_installed() -> str:
    """Return the binary path, or print a hint and exit."""
    binary = _find_binary()
    if binary is None:
        sys.stderr.write(_INSTALL_HINT)
        sys.exit(1)
    return binary


def run(args: list[str]) -> int:
    """
    Run claudectx with the given arguments.
    Returns the exit code.
    """
    binary = _ensure_installed()
    result = subprocess.run([binary, *args])
    return result.returncode


def main() -> None:
    """Entry point for the `claudectx` CLI command installed by pip."""
    # Strip the script name (argv[0]) and forward everything else
    exit_code = run(sys.argv[1:])
    sys.exit(exit_code)
