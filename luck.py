#!/usr/bin/python
#coding: utf-8

"""
Are you in luck ?
Based on original script by Arsh Leak
"""

from random import choice
from time import sleep

luck = ["yes", "no"]

print "Are you in luck?\n>"
sleep(3)

if choice(luck) == luck[0]:
    print "You're in luck!"
else:
    print "You're not in luck."
