#!/usr/bin/env python
# use while true
while True:
   try:
       x=input('Enter the first number:')
       y=input('Enter the second number:')
       value=x/y
       print 'x / y =',value
   except Exception,e:
       print 'Invalid input:',e
       print 'Please try again.'
   else:
       break
