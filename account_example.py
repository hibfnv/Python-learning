#!/usr/bin/python
# -*- coding:utf-8 -*-
# Use python to count the algorithm of salary.
# Author: Eason
print "注意！销售金额请输入数值，切勿输入其它字符。"
try:
    x = int(raw_input("请输入该月销售金额："))
    i = [1000000, 600000, 400000, 200000,100000, 0]
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.10]
    r = 0
    for idx in range(0,6):
        if x > i[idx]:
            r += (x - i[idx]) * rate[idx]
            print (x - i[idx]) * rate[idx]
            x = i[idx]
    print r
except ValueError:
    print "数值输入有误.游戏退出。"