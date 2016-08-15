#!/usr/bin/env python
storage = {}
storage['mid'] = {}
storage['first'] = {}
storage['last'] = {}
a = 'Lambel Starcod Felay'
b = 'Green William George'
storage['first']['Lambel'] = [a]
storage['mid']['Starcod'] = [a]
storage['last']['Felay'] = [a]
storage['first'].setdefault('Green',[]).append(b)
storage['mid'].setdefault('William',[]).append(b)
storage['last'].setdefault('George',[]).append(b)
print storage['first']['Green']
print storage['mid']['Starcod']
####---------------------------####
def init(data):
    data['first'] = {}
    data['mid'] = {}
    data['last'] = {}
storage = {}
init(storage)
print storage
#####
# define lookup
def lookup(data,label,name):
	return data[label].get(name)
print lookup(storage,'mid','Starcod')
