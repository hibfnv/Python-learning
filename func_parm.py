#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Eason
def str(var1,*vartuple):
    print var1
    for var in vartuple:
        print var
print "=" * 20
print "输出定义的变量："
print "=" * 20
str(10)
print "=" * 20
print "输出所有未定义的变量："
print "=" * 20
str(20,30,40)
print "=" * 20