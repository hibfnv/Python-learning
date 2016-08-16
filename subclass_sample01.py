#!/usr/bin/env python
# define a new class for learning about class and objects in session the 7th character
class Bird:
  song="Gua Gua"
  def sing(self):
    print self.song
class SubBird(Bird):
    pass
print '\033[34m=\033[0m' * 30
print '\033[31mUse class:\033[0m'
print '\033[34m=\033[0m' * 30
b=SubBird()
b.sing()
print '\033[34m=\033[0m' * 30
print '\033[31mUse subclass:\033[0m'
print '\033[34m=\033[0m' * 30
g=Bird()
g.sing()
print '\033[34m=\033[0m' * 30
