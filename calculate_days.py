#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a calculate days of years script
# Author: Eason
# 定义两个月份常量，一个是leap为0的平年每月天数的常量列表，一个是leap为1的闰年每月天数的常常量列表
print "日期计算器 "
print "=" * 20
li1 = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]  # 该常量为闰年每月天数的常量列表
li2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 该常量为平年每月天数的常量列表
year = int(raw_input("请输入要计算的公历年份："))
month = int(raw_input("请输入要计算的月份："))
day = int(raw_input("请输入要计算的日期是几号："))
if month > 12 or month <= 0:
    print "请输入[1 - 12]月之间的月份！"
elif day > li1[month - 1] or day > li2[month - 1]:
    print "=" * 20
    print "请输入正确的日期！"
else:
    if year % 4 == 0:
        sum_day = sum(li1[:month - 1]) + day
    else:
        sum_day = sum(li2[:month - 1]) + day
    print "=" * 20
    print "%d年%d月%d日是一年中的第%d天。" % (year, month, day, sum_day)