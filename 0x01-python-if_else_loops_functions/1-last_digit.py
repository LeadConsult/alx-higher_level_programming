#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = f'{number}'
last_digit = num[-1:]

if int(last_digit) > 5:
    print("Last digit of",num,"is",last_digit, "and is greater than 5")
elif int(last_digit) == 0:
    print("Last digit of",num,"is",last_digit, "and is zero")
else:
    print("Last digit of",num,"is",last_digit, "and is less than 6 and not 0")
