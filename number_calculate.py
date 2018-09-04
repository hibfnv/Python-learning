#!/usr/bin/python
# -*- coding:utf-8 -*-
# Calculate the number which it can be sqrt when it plus 100 and plus 268.
# Author: Eason
import math
for i in range(10000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x * x == i + 100) and (y * y == i + 268):
        print i