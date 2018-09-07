#!/usr/bin/python
# -*- coding: utf-8 -*-
# 计算两个for循环的话一共要进行多少次循环操作。
for i in range(1,10):
    for k in range(1,i+1):
        x = k * i
        print "%d x %d = %d " % (k, i, x),
    print "\t"
