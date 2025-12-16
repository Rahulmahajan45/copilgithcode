#!/usr/bin/env python3
"""Read scripts/score.csv and print:
   My name is <column1> , salary <column2> , city <column3>
"""
import csv
import sys
from pathlib import Path

csv_path = Path('scripts/score.csv')

if not csv_path.exists():
    print(f"Error: file not found: {csv_path}", file=sys.stderr)
    sys.exit(1)

with csv_path.open(newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # skip empty rows
        if not row or all(cell.strip() == '' for cell in row):
            continue

        # safely extract columns (use empty string if missing)
        col1 = row[0].strip() if len(row) >= 1 else ''
        col2 = row[1].strip() if len(row) >= 2 else ''
        col3 = row[2].strip() if len(row) >= 3 else ''

       print(f" {col1}") 
       print(f" {col2}") 
       print(f"My name is {col1} , salary {col2} , city {col3}")
