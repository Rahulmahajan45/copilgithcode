#!/usr/bin/env python3
"""
Print a specific row (1-based) from scripts/score.
Usage: python scripts/print_row.py --row 2
"""
import argparse
import sys
from pathlib import Path

SCORE_PATH = Path("scripts/score")

def read_rows(path=SCORE_PATH):
    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(2)
    with path.open() as f:
        lines = [line.rstrip("\n") for line in f if line.strip() != ""]
    # split on commas or whitespace
    rows = [[token.strip() for token in line.replace(",", " ").split()] for line in lines]
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--row", "-r", type=int, required=True, help="1-based row number to print")
    args = parser.parse_args()

    rows = read_rows()
    idx = args.row - 1
    if idx < 0 or idx >= len(rows):
        print(f"Error: row {args.row} out of range (1..{len(rows)})", file=sys.stderr)
        sys.exit(1)

    print(f"Row {args.row}: {' '.join(rows[idx])}")

if __name__ == "__main__":
    main()
