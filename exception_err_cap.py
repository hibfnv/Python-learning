#!/usr/bin/env python
try:
  x=input('Enter the first number:')
  y=input('Enter the second number:')
  print x/y
except (ZeroDivisionError,TypeError,NameError):
  print '\033[31mYour numbers were bogus...\033[0m'
