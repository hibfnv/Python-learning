#!/usr/bin/env python
def plus_num():
	num=input('Enter the number: ')
	if num < 0:
		print "It's a negative number."
	else:
		print 'You type a positive number.'
plus_num()
def hello_1(greeting,name):
	print '%s,%s!' % (greeting,name)
def hello_2(name,greeting):
	print '%s,%s!' % (name,greeting)
print 'this use greeting,name'
hello_1('Hello','World')
print 'this use name, greeting'
hello_2('Hello','World')
print 'this is a split body:'
def hello_3(greeting='Hello',name='World'):
	print '%s, %s!' % (greeting,name)
print hello_3()
print hello_3('Greetings')
print hello_3('Greetings','World')
print hello_3('Greetings','Uiverse')
