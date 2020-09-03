#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Count = 0
    for i in sys.argv[1:]:
        Count += int(i)
    print(Count)
