#!/usr/bin/env python
import os
IP=os.popen('''ifconfig en0|grep "netmask"|awk '{print $2}'|sed 's/addr://g' ''').read()
print IP
