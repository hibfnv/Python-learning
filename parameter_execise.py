#!/usr/bin/env python
def story(**kwds):
	return 'Once upon a time, there was a' \
'%(job)s called %(name)s.' % kwds
story(job='king',name='Gummy')
params={'job':'language','name':'Python'}
story(**params)
del params['job']
story(job='stroke of genius',**params)
##############################################
def power(x,y,*others):
	if others:
		print 'Received redundant parameters:', others
	return pow(x,y)
print power(3,2)
print power(y=3,x=2)
params=(5,) * 2
print power(*params)
print power(3,3,'Hello,World')
