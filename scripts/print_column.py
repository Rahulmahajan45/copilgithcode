#!/usr/bin/env python3
"""
Print a specific column (1-based) from scripts/score.
Usage: python scripts/print_column.py --col 3
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
    rows = [[token.strip() for token in line.replace(",", " ").split()] for line in lines]
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--col", "-c", type=int, required=True, help="1-based column number to print")
    args = parser.parse_args()

    rows = read_rows()
    col_idx = args.col - 1
    if col_idx < 0:
        print(f"Error: column must be >= 1", file=sys.stderr)
        sys.exit(1)

    print(f"Column {args.col}:")
    for i, row in enumerate(rows, start=1):
        if col_idx < len(row):
            print(row[col_idx])
        else:
            print("")  # print empty line for missing values

if __name__ == "__main__":
    main()
