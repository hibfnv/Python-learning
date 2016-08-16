#!/usr/bin/env python
def checkindex(key):
  if not isinstance(key,(int,long)):
    raise TypeError
  if key < 0:
    raise IndexError
class AthimeticSequence:
  def __init__(self,start=0, step=1):
    self.start=start
    self.step=step
    self.changed={}
  def __getitem__(self,key):
    checkindex(key)
    try:
      return self.changed[key]
    except KeyError:
      return self.start + key*self.step
  def __setitem__(self,key,value):
    checkindex(key)
    self.changed[key]=value
    s=AthimeticSequence(1,2)
    print 'key as 4 get value result'
    print s[4]
    print 'set key as 4 value as 2'
    s[4]=2
    print s[4]
    print 'key as 5 get value result'
    print s[5]
