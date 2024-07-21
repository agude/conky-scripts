#!/usr/bin/python
import subprocess

string = subprocess.getoutput('nvidia-settings -q gpucoretemp -t')
split_string = string.splitlines()
print(split_string[0])
