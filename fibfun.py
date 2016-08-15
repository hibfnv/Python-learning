#!/usr/bin/env python
fibs=[0, 1]
def fibs():
	num=int(input('Enter a number: '))
	result = [0, 1]
	for i in range(num-2):
	    result.append(result[-2] + result[-1])
	return result
print fibs()
