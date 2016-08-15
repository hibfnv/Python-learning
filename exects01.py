#!/usr/bin/env python
# This is a exec script for python
from math import sqrt
scope={}
x=int(input('Enter a number: '))
exec 'sqrt =1' in scope
print sqrt(x)
