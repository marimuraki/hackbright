#!/bin/env python

"""
Given the string s, split it into two strings, s2 and s3, s2 containing the first 5 letters of the string, and s3 containing the remaining letters.

eg:
    s1 = "Hello there"
    s2 = "Hello"
    s3 = " there"

"""

s = "Hi there, my name is Slim"

s2 = s[0:5]
s3 = s[5:]

print s2
print s3
