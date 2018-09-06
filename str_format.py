#!/usr/bin/python
# -*- coding:utf-8 -*-
products = raw_input("请输入商品名称：")
weight = input("请输入计重：")
price = input("请输入计量价格：")
width = 24
price_width = 8
weight_width = 8
print "\n"
print "=" * width
print "\tItem:"
prices = weight * price
item_width = width - weight_width - price_width
first_format = '%-*s%*s%*s'
b_format = '%-*s%*.2f%*.2f'
print "=" * width
print first_format % (item_width, 'Item', weight_width, 'Weight', price_width, 'Total')
print '-' * width
print b_format % (item_width, products, weight_width, weight, price_width, prices)
print '-' * width
print '=' * width