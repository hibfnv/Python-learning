#!/usr/bin/env python
def with_stars(**kwds):
	print kwds['name'],'is',kwds['age'],'years old'
def without_stars(kwds):
	print kwds['name'],'is',kwds['age'],'years old'
args={'name':'Mr.Gummy','age':42}
with_stars(**args)
print 'above is with stars in function.'
without_stars(args)
print 'above is without stars in function.'
######################################################
def foo(x,y,z,m=0,n=0):
	print x,y,z,m,n
def call_foo(*args,**kwds):
	print "Calling foo!"
	foo(*args,**kwds)
