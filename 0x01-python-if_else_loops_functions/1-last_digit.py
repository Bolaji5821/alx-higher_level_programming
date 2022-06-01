#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
str = f"Last digit of {number} is {last_digit} and is"
if last_digit > 5:
    print(f"{str} greater than 5")
elif last_digit == 0:
    print(f"{str} is 0")
elif last_digit < 6:
    print(f"{str} less than 6 and not 0")
