#!/usr/bin/python
# -*- coding:utf-8 -*-
# 使用斐波那契函数，先定义一个空的列表，然后使用追加方法进行逐个增加值。
k = int(raw_input("请输入需要获得的值的个数："))
x = []
for i in range(k):
    if i == 0 or i == 1:
        x.append(1)
    else:
        x.append(x[i - 2] + x[i - 1])
print x
