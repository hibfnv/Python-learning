#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a dictionary script
# Author: Eason
import json
dict = {}
print "请输入姓名、年龄和部门，谢谢。"
dict ['姓名'] = raw_input("姓名: ")
dict['年龄'] = raw_input("年龄: ")
dict['部门'] = raw_input("所属部门：")
dicts = json.dumps(dict,encoding='utf-8',ensure_ascii=False)
print "该字典为：", dicts
