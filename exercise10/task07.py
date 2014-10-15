#!/bin/env python

"""
Given the list l composed of tuples, sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""

import operator

l = [(1,2), (3,1), (17, 35), (81,20)]

print sorted(l, key=lambda x: x[1])

l.sort(key=lambda x: x[1])

print l

l.sort(key=operator.itemgetter(1))

print l