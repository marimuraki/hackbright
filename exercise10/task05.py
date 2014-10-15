#!/bin/env python

"""
Given the string s, excise characters 6 through 12, inclusive
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"
"""

s = "Hi there, my name is Slim"

print s[0:5] + s[11:]
