#!/usr/bin/python3
if __name__ == "__main__":
    import sys len(sys.argv)
    for i in range(len(sys.argv)):
        if i == 0:
            print("0 arguments.")
        elif i == 1:
            print("1 argument:", "i", ":", "argv", end="\n")
        else:
            print(len(sys.argv), "arguments:", "i", ":", "argv", end="\n")
