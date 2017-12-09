#!/usr/bin/env python
while True:
	score=input('Enter the score for test: ')
	if score == 100:
		print 'The score is Super A.'
		break
	elif  100 > score >= 90:
		print 'The score is A.'
		break
	elif 90 > score >= 80:
		print 'The score is B.'
		break
	elif 80 > score >= 70:
		print 'The score is C.'
		break
	elif 70 > score >= 60:
		print 'The score is D.'
		break
	elif 0 < score < 60:
		print 'Worse score F.'
		break
	else:
		print 'Invalid number input.Try again.'
