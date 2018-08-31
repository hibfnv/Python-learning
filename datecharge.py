#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a date interchange testing program .
# Author : Eason Xu
# Define months interchange.
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
# Define date ends.
ends = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
a_year = raw_input("Please enter years: ")
a_month = raw_input("Enter inquiry month: ")
a_day = raw_input("Enter inquiry day: ")
if a_year.isalpha() or a_month.isalpha() or a_day.isalpha():
    print "Please make sure you enter is integrate digital number."
elif a_year.isdigit() and a_month.isdigit() and a_day.isdigit():
    n_year = int(a_year)
    n_month = int(a_month)
    n_day = int(a_day)
    if n_year <= 0 or n_year > 2100 or n_month <=0 or n_month > 12 or n_day <=0 or n_day > 31:
        print "Please make sure year[1 - 2100], month[ 1 - 12] and day [1 - 31]."
    else:
        month_name = months[n_month -1]
        day_name = a_day + ends[n_day -1]
        print "The Date is " + month_name + ' ' + day_name +', ' + a_year
else:
    print "\n"