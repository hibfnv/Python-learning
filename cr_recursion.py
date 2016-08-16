#!/usr/bin/env python
print '\033[34m=\033[0m' * 30
def flat(nested):
    try:
        try:
            nested+''
	except TypeError:
	    pass
	else:
	    raise TypeError
	for sublist in nested:
	    for element in flat(sublist):
		yield element
    except TypeError:
	yield nested
print list(flat(['foo',['bar',['baz']]]))
##############################################
print '\033[34m=\033[0m' * 30
def flatten(nested):
	try:
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested
print list(flatten([[[1],2],3,4,[5,[6,7]],8]))
print '\033[34m=\033[0m' * 30
