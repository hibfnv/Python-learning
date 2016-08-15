#!/usr/bin/env python
dict={'x':1,'y':2,'z':3}
for key,value in dict.items():
	print key,'corresponds to',value
################################################
print '**' * 20
print 'User the old method:'
for key in dict:
	print key, 'corresponds to', dict[key]
##====================================================
print '=='*20
names=['anne','beth','george','damon']
ages=[12,45,32,102]
for i in range(len(names)):
	print names[i],'is',ages[i],'years old.'
print '##' * 20
##----------------------------------------------------
print zip(names,ages)
for name,age in zip(names,ages):
    print name,'is',age,'years old.'
