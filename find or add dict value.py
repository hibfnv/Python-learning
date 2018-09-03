#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a dictionary script
# Author: Eason
import json
dict = {}
flag = 'a'
tod = 'p'
di = 'n'
while flag == 'a' or tod == 'p':
    flag = raw_input("请输入选择项,(a)添加姓名，(s)查找姓名: ")
    if flag == 'a':
        print "请输入姓名、年龄和部门，谢谢。"
        dict ['姓名'] = raw_input("姓名: ")
        dict['年龄'] = raw_input("年龄: ")
        dict['部门'] = raw_input("所属部门：")
        print "添加成功。"
        tod = raw_input("查看添加的字典，(p)查看：")
        if tod == 'p':
            dicts = json.dumps(dict,encoding='utf-8',ensure_ascii=False)
            print "该字典为：", dicts
        else:
            continue
    elif flag == 's':
        ch_word = raw_input("请输入查找的姓名：")
        for key in sorted(dict.values()):
            if str(ch_word) == key:
                dicts = json.dumps(dict, encoding='utf-8', ensure_ascii=False)
                print key, dicts
                break
        else:
            di == 'n'
            print "字典中不存在该姓名。"
    else:
        print "输入出错，执行结束。"
        break
