#!/usr/bin/python
# -*- coding:utf-8 -*-
# Class of Employeer information.
# Author: Eason
class empinfo:
    emp_id = 0

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept
        empinfo.emp_id += 1

    def dis_id(self):
        print "Total employee is: %d" % empinfo.emp_id

    def dis_info(self):
        print '''Username: %s, Age is %d, User's Department is %s.''' % (self.name, self.age, self.dept)


empstr1 = empinfo('Lorry', 23, 'HR')
empstr2 = empinfo('Browns', 45, 'FA')
empstr1.dis_info()
empstr2.dis_info()
print "Total employee is %d" % empinfo.emp_id