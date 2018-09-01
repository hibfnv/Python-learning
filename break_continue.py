#!/usr/bin/python
# -*- coding:utf-8 -*-
# this is a conditional script of break and continue
# Author : Eason
# Break condition when script functioned
print "=" * 30
for letter in 'Python':
    if letter == 'h':
        break
    print letter
print "=" * 30
var = 10
while var > 0:
    print var
    var = var - 1
    if var == 5:
        break
print "=" * 30
# Continue condition when script functioned
for letters in 'Python':
    if letters == 'h':
        continue
    print letters
print "=" * 30
i = 10
while i > 0:
    print i
    i = i - 1
    if i == 5:
        continue
print "=" * 30
print "执行结束，退出。"
