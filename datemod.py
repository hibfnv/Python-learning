#!/usr/bin/env python
# Change Date 0000-00-00 to YY-Aug_month-Day_st
# define mon cmon day c_day mon_char

# user input
year = raw_input('Enter the current year: ')
mon = raw_input('Enter the current month[1-12]: ')
day = raw_input('Enter the current day[1-31]: ')

# begin list charge list
cmon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# day extend
ext = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']

# charge string to int
mon_no = int(mon)
day_no = int(day)
# use month,day's number as index in list
mon_char = cmon[mon_no-1]
c_day = day+ext[day_no-1]
# print all changed string
print mon_char + ' ' + c_day + ',' + year
