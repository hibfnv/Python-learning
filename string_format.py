#!/usr/bin/env python
# Learning about string format session
width = int(raw_input('Enter a width number: '))
ori_width = 12
main_width = width - ori_width
# define string format as title_format and main_format
title_format = '%-*s%*s'
main_format = '%-*s%*.2f'
# split line in body
print '\033[34m=\033[0m' * width
print title_format % (main_width, 'Menu', ori_width, 'Price')
# split line in body
print '\033[34m-\033[0m' * width
print main_format % (main_width, 'Apple', ori_width, 0.6)
print main_format % (main_width, 'Banana', ori_width, 2)
print main_format % (main_width, 'Carrot', ori_width, 6)
print main_format % (main_width, 'Tomato', ori_width, 3.8)
print main_format % (main_width, 'Pear', ori_width, 1.26)
print main_format % (main_width, 'Peach', ori_width, 0.8)
# end line
print '\033[34m=\033[0m' * width
print '\033[31mNotice: Please checkout your menu when leave out.\033[0m'
