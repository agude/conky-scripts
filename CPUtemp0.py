#!/usr/bin/python
import commands

string = commands.getoutput('cat /sys/devices/platform/coretemp.0/temp1_input')
#temp = float( int(string) / 1000 ) + 10.0
temp = float( int(string) / 1000 ) + 10
print temp
