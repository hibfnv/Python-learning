#!/usr/bin/env python
# define fibs
fibs = [0, 1]
num = input('Enter number for fibo_math: ')
for i in range(num - 2):
    fibs.append(fibs[-2] + fibs[-1])
print fibs
