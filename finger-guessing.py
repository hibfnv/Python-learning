#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a finger-guessing small game
# At first we defined three number for user choice in put!
# Then let computer random to choose
# Author: Eason
import random
while 1:
    print "Finger-guessing game use '1' for '石头','2' for '剪刀', '3' for '布' and 'e' for exit. "
    s = int(random.randint(1, 3))
    a = raw_input("Please enter your guess: ")
    test_list = ['石头', '剪刀', '布']
    if a.isalpha():
        if (a not in test_list) and (a == 'e'):
            print "退出游戏。"
            break
    elif a.isdigit():
        m = int(a)
        if s == 1:
            ind = "石头"
            if m == 1:
                print "系统出"+ ind + ",你们是平局。"
            elif m == 2:
                print "系统出"+ ind + ",很遗憾，你输了。"
            elif m == 3:
                print "系统出"+ ind + ",恭禧你，你赢了。"
        if s == 2:
            ind = "剪刀"
            if m == 2:
                print "系统出"+ ind + ",你们是平局。"
            elif m == 3:
                print "系统出"+ ind + ",很遗憾，你输了。"
            elif m == 1:
                print "系统出"+ ind + ",恭禧你，你赢了。"
        if s == 3:
            ind = "布"
            if m == 3:
                print "系统出"+ ind + ",你们是平局。"
            elif m == 1:
                print "系统出"+ ind + ",很遗憾，你输了。"
            elif m == 2:
                print "系统出"+ ind + ",恭禧你，你赢了。"
        elif (m not in test_list) and (m != s):
            print "输入错误，请重新输入："