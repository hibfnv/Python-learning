#!/usr/bin/env python
class rectangle:
  def __init__(self):
    self.width=0
    self.height=0
  def setsize(self,size):
    self.width,self.height=size
  def getsize(self):
    return self.width,self.height
r=rectangle()
r.width=10
r.height=5
print r.getsize()
r.setsize((150,100))
print r.width
