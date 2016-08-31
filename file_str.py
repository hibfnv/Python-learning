#!/usr/bin/env python3.5
f=open(r'/home/eaxu/workspace/Python_Scripts/somefile.txt','w')
f.write('Welcome to this file,There is nothing here expect.This is stupid to showing.')
f.close
f=open(r'/home/eaxu/workspace/Python_Scripts/somefile.txt')
print f.read()
f.close
