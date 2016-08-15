#!/usr/bin/env python
# if conitional script
name=raw_input('\033[34mEnter your name: \033[0m')
if name.endswith('Tsui'):
	if name.startswith('Mr.'):
		print '\033[31mGreetings! Mr. Tsui\033[0m'
	elif name.startswith('Mrs.'):
		print '\033[35mGreetings, Mrs. Tsui\033[0m'
	else:
		print '\033[36mGreetings, Tsui\033[0m'
elif name.endswith('Lillian'):
		print "\033[34mGreetings!!My Lovely girl,Lillian\033[0m"
else:
	print '\033[32mGreetings, everyone!!\033[0m'
