#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    ld = number % 10
else:
    ld = (number * -1) % 10
    ld = ld * -1

if ld > 5:
    print(f"Last digit of {number:d} is {ld:d} and is greater than 5")
elif ld < 6 and ld != 0:
    print(f"Last digit of {number:d} is {ld:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {ld:d} and is 0")
