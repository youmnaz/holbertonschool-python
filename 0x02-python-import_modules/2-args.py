#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv == 1):
        print("1 argument:")
    else:
        print(len(argv), "arguments:")
    for i in range(0, len(argv)):
        print(i, ":", argv[i], end="")
