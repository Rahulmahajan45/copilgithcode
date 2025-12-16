#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: concat.py <string1> <string2>")
        sys.exit(1)

    s1 = sys.argv[1]
    s2 = sys.argv[2]

    # Concatenate without any separator. Change to f"{s1} {s2}" to add a space.
    result = s1 + s2
    print(result)

if __name__ == "__main__":
    main()
