#!/usr/bin/env python
# Begin script by python
# define variables in use
dict={}
dict['first']={}
dict['middle']={}
dict['last']={}
# initializa info
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
dict={}
init(dict)
print dict
# add info below:
me='Green George Will'
dict['first']['Green']=[me]
dict['middle']['George']=[me]
dict['last']['Will']=[me]
print dict['middle']['George']
# add more info here
my_sister='Alice Princess Will'
dict['first'].setdefault('Alice',[]).append(my_sister)
dict['middle'].setdefault('Princess',[]).append(my_sister)
dict['last'].setdefault('Will',[]).append(my_sister)
print dict['first']['Alice']
# get middle name here
print '\033[34m=\033[0m'*12
print 'Get middle name here:'
print dict['middle']
print 'Get last name'
print dict['last']
print 'Get last name which called Will'
print dict['last']['Will']
print '\033[34m-\033[0m'*12
# define a lookup function
def lookup(data,label,name):
    return data['lable'].get(name)
print lookup(dict,'middle','George')
print lookup(dict,'last','Will')
