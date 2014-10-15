#!/bin/env python

"""
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
"""

import operator

d = {"q": 5, "m": 3, "z":2, "a": 10}

# sort by keys

sorted_keys_d = sorted(d.items(), key=operator.itemgetter(0))

# sort by values

sorted_values_d = sorted(d.items(), key=operator.itemgetter(1))

# sorted dictionary

print "dictionary"
print d
print "sorted by key"
print sorted_keys_d
print "sorted by value"
print sorted_values_d
