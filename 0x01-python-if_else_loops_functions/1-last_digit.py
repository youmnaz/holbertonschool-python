#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if number < 0:
    last_digit *= -1
if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5", end ="")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0", end = "")
elif last_digit < 6 and last_digit != 0:
    print("Last digit of", number, "is", last_digit, "and is less than 6 and no\t 0", end = "")
else:
    print("Last digit of", number, "is", last_digit, "and is 0", end = "")
