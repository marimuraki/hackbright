#!/bin/env python

"""
Given a multiline string 's', print each line along with the line number

eg:
    s = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

"""

text = "Sorry,\nMy people need me\nI must go"

l = [s.strip() for s in text.splitlines()]

counter = 1
for i in range(len(l)):
	print counter, l[i]
	counter += 1
