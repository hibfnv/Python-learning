#!/usr/bin/python
# -*- coding:utf-8 -*-
# This is a system OS check script that used to check your system and PC name.
# Author: Eason
import sys,platform
def os_platform():
    os = platform.system()
    os_plat = platform.platform()
    arch = platform.architecture()
    os_node = platform.node()
    os_ver = platform.version()
    print "Your Operation System is: ", os
    print "Your System Architecture is ", arch
    print "Your System Platform is ", os_plat
    print "Your PC Name is ", os_node
    print "Your OS version is ", os_ver
os_platform()