#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum = 0
    c = len(sys.argv) - 1

    if c == 0:
        print(0)

    if c > 0:
        for i in range(c):
            sum = sum + int(sys.argv[i + 1])
        print(sum)
