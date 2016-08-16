#!/usr/bin/env python
# use __metaclass__=type super function can only work in newest class type
__metaclass__=type //* Only work about python 3.0 and above *//
class Bird:
  def __init__(self):
    self.hungry=True
  def eat(self):
    if self.hungry:
      print 'Aaaah...'
      self.hungry=False
    else:
      print 'No,thanks.'
class SubBird(Bird):
  def __init__(self):
    super(SubBird,self).__init() //* Only work about python 3.0 and above *//
    Bird.__init__(self) //* work under python 3.0 *//
    self.song='Squaawk!!'
  def sing(self):
    print self.song
sb=SubBird()
print '\033[35m When Bird is singing:\033[0m'
sb.sing()
print '\033[32mwhen Bird is hungry:\033[0m'
sb.eat()
print '\033[34mwhen Bird is full:\033[0m'
sb.eat()
