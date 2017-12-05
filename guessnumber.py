#!/usr/bin/env python
import random
guess=random.randint(1,100)
i=0
while i<10: 
     temp = input('Enter a number you guess[0-100]: ')
     if temp == guess:
	print 'Well done, you got the just number!'
	break
     if temp < guess:
	print 'You guess number is small,try again.'
        i += 1
	print 'You have ',10-i,' times.'
     else:
	print 'You guess number is bigger,try again.'
	i += 1
	print 'You have ',10-i,' times.'
else:
	print 'Game over, you waste three times.'

