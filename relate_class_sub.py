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
b=Bird()
print '\033[34m=\033[0m' * 30
b.eat()
print '\033[34m=\033[0m' * 30
print 'use the same method again will show:
print '\033[34m=\033[0m' * 30
b.eat()
print '\033[34m=\033[0m' * 30
