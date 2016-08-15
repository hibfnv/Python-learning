#!/usr/bin/env python
# define a empty dictionary
d={}
d['first']={}
d['middle']={}
d['last']={}
# define a initialize function
def init(data):
	data['first']={}
	data['middle']={}
	data['last']={}
init(d)
def lookup(data,label,name):
	return data[label].get(name)
def store(data,*full_names):
	for full_name in full_names:
		names=full_name.split()
		if len(names) == 2:
			names.insert(1,' ')
		labels=('first','middle','last')
		for label,name in zip(labels,names):
			people=lookup(data,label,name)
		if people:
			people.append(full_name)
		else:
			data[label][name]=[full_name]
store(d,'Han Solo')
store(d,'Luke Skywalker','Anakin Skywalker')
print lookup(d,'last','Skywalker')
