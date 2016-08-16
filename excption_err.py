#!/usr/bin/env python
try:
  x=input('Enter the fist number:')
  y=input('Enter the second number:')
  print x/y
except (ZeroDivisionError,TypeError),e:
  print e
