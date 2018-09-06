#!/usr/bin/python
# -*- coding:utf-8 -*-
# simple dictionary for search keys.
# Author: Eason
# 用户简单数据库
people = {
    'Alice':{
    'phone':'2341','addr':'Miami'
},
    'Tom':{
        'phone':'9102','addr':'Hawaii'
    },
    'Jimmy':{
        'phone':'3221','addr':'Boston'
             }
}
labels = {
    'phone':'Phone number',
    'addr':'Address'
          }
name = raw_input("请输入用户名：")
request = raw_input('Please chose[p] for phone,[a] for adress: ')
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
if name.capitalize() in people:
    c_name = name.capitalize()
    print "%s's %s is %s." % (c_name, labels[key],people[c_name][key])