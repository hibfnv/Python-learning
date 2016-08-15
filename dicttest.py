#!/usr/bin/env python
#
# This is a dictionary test by python
#
people = {
   'Alice' : { 'phone' : '2101',
             'address' : 'No.1 st,PH,US'
             },
   'Betch' : { 'phone' : '2155',
               'address' : 'No.172,Wall St,US'
             },
   'Cecil' : { 'phone' : '3106',
               'address' : 'No.291,LA,US'
             }
         }
labels = { 'phone' : 'phone number',
           'addr' : 'address'
         }
name = raw_input('Name: ')
request = raw_input('Please chose[p] for phone,[a] for adress: ')
if request == 'p' : key = 'phone'
if request == 'a' : key = 'address'
if name in people : print "%s's %s is %s." % (name, labels[key], people[name][key])
