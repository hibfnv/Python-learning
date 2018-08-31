#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Eason
rows = int(input("Enter number you wanna: "))
for a in range(0, rows):
    if a == rows - 1:
        for k in range(2 * rows - 1):
            if k % 2 == 0:
                print "*",
            else:
                print " ",
    else:
        for j in range(2 * rows - 1):
            if (j == (2 * rows -1) // 2 - a) or (j ==(2 * rows - 1) // 2 + a):
                print "*",
            else:
                print " ",
    print "\n"
