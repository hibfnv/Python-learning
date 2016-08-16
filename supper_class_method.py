#!/usr/bin/env python
class Bird:
  def __init__(self):
    self.hungry=True
  def eat(self):
    if self.hungry:
      print 'Aaaah...'
      self.hungry=False
    else:
      print 'No, thanks.'
class SubBird(Bird):
  def __init__(self):
    Bird.__init__(self)
    self.song='Squaawk!!'
  def sing(self):
    print self.song
sb=SubBird()
sb.sing()
print '\033[31mget Bird eat() function method, which it is named bind:\033[0m'
sb.eat()
