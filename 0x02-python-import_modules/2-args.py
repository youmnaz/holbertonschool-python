#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len(sys.argv)
    for i in range(1, len(sys.argv)):
        if len(sys.argv) == 0:
            print("0 arguments.")
        elif len(sys.argv) == 1:
            print("1 argument", "/n", i, ":", argv[i], end="")
        else:
            print(len(sys.argv), ":", "arguments", "/n", "i", ":", argv[i],
                  end="/n")
