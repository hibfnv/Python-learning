#!/usr/bin/python
# -*- coding:utf-8 -*-
x = int(raw_input("请输入一个有效的自然数："))  # 此处数值为前两个数值相加之和要小于输入的数值。
a = 0
b = 1
while b < x:
    print b,
    a,b = b, a+b