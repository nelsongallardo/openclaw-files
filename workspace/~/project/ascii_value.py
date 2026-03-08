#!/usr/bin/env python3
"""Convert input string(s) to ASCII values."""

import sys


def to_ascii(text: str) -> list[int]:
    """Convert a string to a list of ASCII values."""
    return [ord(c) for c in text]


def main():
    # Get input: command line args if provided, else stdin
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
    else:
        input_text = sys.stdin.read().rstrip("\n")

    if not input_text:
        print("No input provided", file=sys.stderr)
        sys.exit(1)

    ascii_values = to_ascii(input_text)
    
    # Output: space-separated values
    print(" ".join(str(v) for v in ascii_values))
    
    # Also show the mapping
    mapping = " ".join(f"{c}({v})" if c.isprintable() else f"\\x{ord(c):02x}({v})" for c, v in zip(input_text, ascii_values))
    print(f"Mapping: {mapping}")


if __name__ == "__main__":
    main()
