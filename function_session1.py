#!/usr/bin/env python
dict={}
dict['first']={}
dict['middle']={}
dict['last']={}
# initialize data
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
init(dict)
print dict
# add user info
me='Green George Will'
dict['first']['Green']=[me]
dict['middle']['George']=[me]
dict['last']['Will']=[me]
print dict['middle']['George']
my_sister='Alice Princess Will'
dict['first'].setdefault('Alice',[]).append(my_sister)
dict['middle'].setdefault('Princess',[]).append(my_sister)
dict['last'].setdefault('Will',[]).append(my_sister)
print dict['first']['Alice']
print 'Print middle name here:'
print dict['middle']['George']
print 'Print last name here: '
print dict['last']['Will']
print 'Get middle name'
print dict['middle']
print 'get last name'
print dict['last']
# define lookup function
def lookup(data,label,name):
    return data[label].get(name)
print lookup(dict,'middle','George')
print lookup(dict,'last','Will')
