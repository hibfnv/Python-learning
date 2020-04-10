#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a random number compare and sequence in queue script.
# Author: Eason
print "随机数字输入及排序"
print "=" * 20
x = []
for i in range(3):
    a = int(raw_input("请随机输入一个数字："))
    x.append(a)
x.sort()
print "=" * 20
print x
