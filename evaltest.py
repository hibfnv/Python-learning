#!/usr/bin/env python
# eval provide another named space, and it used to be like this
# if you use eval(raw_input(...)), in fact it is change this user input
# as input(...)
scope={}
scope['x']=2
scope['y']=3
print eval('x*y',scope)

####################################

scope={}
exec 'x=2' in scope
print eval('x*x',scope)
