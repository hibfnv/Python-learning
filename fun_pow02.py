#!/usr/bin/env python
n=input('Enter the number:')
def pow_name(n):
	if n == 1:
		return 1
	else:
		return n * pow_name(n-1)
print pow_name(n)
print '\033[34m=\033[0m'*30
# define new recrusion in same method
def pow_p(x,n):
	result = 1
	for i in range(n):
		result *= x
	return result
print pow_p(3,9)
print '\033[34m=\033[0m'*30
def pow_x(x,n):
	if n == 0:
		return 1
	else:
		return x * pow_x(x,n-1)
print pow_x(16,4)
print '\033[34m=\033[0m'*30
