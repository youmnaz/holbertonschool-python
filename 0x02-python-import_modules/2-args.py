#!/usr/bin/python3
if __name__ == "__main__":
    import sys
        if len(sys.argv) == 1:
            print("0 arguments.")
        elif len(sys.argv) == 2:
            print("1 argument:")
            print("1: {}".format(sys.argv[1]))
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
            count = 0
            for i in sys.argv[1:]:
                count = count + 1
                print("{}: {}".format(count, i))
