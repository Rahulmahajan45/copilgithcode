#!/usr/bin/env python3
"""
Find and print the row with the highest total score (sum of numeric columns).
Usage: python scripts/highest_row.py
"""
import sys
from pathlib import Path

SCORE_PATH = Path("scripts/score.csv")

def parse_row_to_floats(row):
    vals = []
    for token in row:
        try:
            vals.append(float(token))
        except ValueError:
            # ignore non-numeric tokens when computing sum
            pass
    return vals

def read_rows(path=SCORE_PATH):
    if not path.exists():
        print(f"Error: {path} not found.", file=sys.stderr)
        sys.exit(2)
    with path.open() as f:
        lines = [line.rstrip("\n") for line in f if line.strip() != ""]
    rows = [[token.strip() for token in line.replace(",", " ").split()] for line in lines]
    return rows

def main():
    rows = read_rows()
    if not rows:
        print("No rows in score file.", file=sys.stderr)
        sys.exit(1)

    best_index = None
    best_sum = None
    for i, row in enumerate(rows):
        nums = parse_row_to_floats(row)
        total = sum(nums) if nums else 0.0
        if best_sum is None or total > best_sum:
            best_sum = total
            best_index = i

    print(f"Row with highest score: {best_index+1}")
    print(f"Sum: {best_sum}")
    print(f"Row {best_index+1}: {' '.join(rows[best_index])}")

if __name__ == "__main__":
    main()
