#!/usr/bin/env python
x=1
scope=vars()
print scope['x']
scope['x'] += 1
print x

