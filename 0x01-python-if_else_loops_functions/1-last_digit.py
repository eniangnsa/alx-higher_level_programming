#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number)
last = int(str(num)[-1])
if last > 5:
    print(f"Last digit of {num:d} is {last:d} and  is greater than 5")
elif last == 0:
    print(f"Last digit of {num:d} is {last:d} and  is 0")
else:
    print(f"Last digit of {num:d} is {last:d} and  is less than 6 and not 0")
