#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_arg = 0
    num_arg = len(sys.argv) - 1
    for i in range(num_arg):
        total_arg += int(sys.argv[i + 1])
    print("{}.format(total_arg))
