# !/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    function that returns
    min operation numbers
    """
    if type(n).__name__ != int.__name__:
        return 0
    elif n <= 0:
        return 0
    else:
        CurrStr = "H"
        count = 0
        TargetStr = "H" * n
        while len(CurrStr) != len(TargetStr):
            if len(CurrStr) < len(TargetStr) / 2:
                addStr = CurrStr
                count += 1
            CurrStr = CurrStr + addStr
            count += 1
            if len(CurrStr) + len(addStr) <= len(TargetStr):
                CurrStr = CurrStr + addStr
                count += 1
        return count
