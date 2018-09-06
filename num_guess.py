#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a game of guess number and it is advanced one
# Author: Eason
import random
i = random.randint(1, 100)
n = 0
while True:
    x = int(raw_input("请输入你猜测的数字："))
    n += 1
    if x > 100 or x < 0:
        print "请输入1 - 100之间的数字。"
    elif x < i:
        print "你所猜测的数值过小。"
    elif x > i:
        print "你所猜测的数值过大。"
    else:
        print "恭禧你成功猜中了给定的数字。你一共猜测了%d次。" % n
        break