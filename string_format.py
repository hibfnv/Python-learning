#!/usr/bin/env python
# use string format in this session
width = int(raw_input('Enter a width number[0-50]: '))
ori_width = 12
main_width = width - ori_width
# define string format title_format and main_format
title_format = '%-*s%*s'
main_format = '%-*s%*.2f'
# split body with ====
print '\033[34m=\033[0m' * width
print title_format % (main_width, 'Menu', ori_width, 'Price')
# split body with -----
pirnt '\033[34m-\033[0m]' * width
print main_format % (main_width, 'Apple', next_width, '0.8')
print main_format % (main_width, 'Apple', next_width, '0.8')
