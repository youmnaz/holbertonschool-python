# !/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = int(a)/int(b)
        return quotient
    except ZeroDivisionError:
        quotient = None
        return quotient
    finally:
        print("Inside result: {}".format(quotient))
