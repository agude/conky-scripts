#!/usr/bin/python
import commands

string = commands.getoutput('nc localhost 7634')
list = string.split('|')
print list[list.index('/dev/sdb')+2]
