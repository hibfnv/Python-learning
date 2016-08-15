#!/usr/bin/env python
num=int(raw_input('Please enter a number: '))
if num < 0:
   print '\033[31mThe number is negative.\033[0m'
elif num > 0:
   print '\033[36mThe number is positive\033[0m'
else:
   print '\033[34mThe number you typed is %s\033[0m' % num
