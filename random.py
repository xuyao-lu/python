#!/usr/bin/env python
# coding=utf-8
import random
data = random.randint(1,5)
guess = int (input("Pleast inter your number(1-5):"))
if guess == data:
    print("Good job!\n It's  %d"%data)
else:
    print("Wrong ! \nIt's  %d"%data)

