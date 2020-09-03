#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for i in range(0, len(argv)):
        if i == 0:
            print("0 arguments.")
        elif i == 1:
            print("1 argument:", "i:", "argv[i]", end="\n")
        else:
            print(len(argv), "arguments:", "i:", "argv[i]", end="\n")
