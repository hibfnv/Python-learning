#!/usr/bin/python
# This is a sentence rectangle
# Author: Eason
sentence = raw_input("Input your sentences:")
screen_width = 120
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print
print ' ' * left_margin + '+' + '-' * (box_width - 6) + '+'
print ' ' * left_margin + '|' + ' ' * text_width + '|'
print ' ' * left_margin + '|' + sentence + '|'
print ' ' * left_margin + '|' + ' ' * text_width + '|'
print ' ' * left_margin + '+' + '-' * (box_width - 6) + '+'
print
