#!/usr/bin/env python
import sys

try:
	filename=sys.argv[1]
	try:
		f=file(filename)
	except IOError:
		print 'File is not exist!'
		sys.exit()
	while True:
		line=f.readline()
		if len(line)==0:
			break
		print line
	f.close()
except IndexError:
	print 'USAGE:Python %s filename' % sys.argv[0]
