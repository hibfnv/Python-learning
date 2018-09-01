#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a while loop scripts
# Author : Eason
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > (i / j):
        print i, "是素数。"
    i = i + 1
print "执行结束，退出。"
