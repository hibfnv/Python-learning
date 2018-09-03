#!/usr/bin/python
# -*- coding:utf-8 -*-
# import time module
# Author: Eason
import time
local_time = time.localtime(time.time())
time = time.time()
print "=" * 24
print "累计从1970年到现在的总累计时间"
print time
print "=" * 24
print "本地时间是：", local_time
print "=" * 24
