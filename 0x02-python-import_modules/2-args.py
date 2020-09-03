#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len(sys.argv)
    for i in range(len(sys.argv)):
        if i == 0:
            print("0 arguments.")
        elif i == 1:
            print(i, ":", "argument", "/n", "i", ":", "argv", end="")
        else:
            print(len(sys.argv), ":", "arguments", "/n", "i", ":", "argv", end="/n")
