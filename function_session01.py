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
