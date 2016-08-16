#!/usr/bin/env python
def hello(greeting,name):
	print '%s, %s!' % (greeting,name)
param={'name':'Sir Robin','greeting':'Well met'}
hello(**param)
