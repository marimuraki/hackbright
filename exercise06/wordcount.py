# Source: https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise06

"""
Problem Description
-------------------
Write a program, wordcount.py, that opens a file named on the command
line and counts how many times each space-separated word occurs in
that file. Your program should then print those counts to the
screen. 
       
 """

from sys import argv
import string
from operator import itemgetter

script, filename = argv

f = open(filename)
filetext = f.read()

"""
Exclude punctuation

set(['!', '#', '"', '%', '$', "'", '&', ')', '(', '+', '*', '-', ',', '/', '.', ';', ':', '=', '<', '?', '>', '@', '[', ']', '\\', '_', '^', '`', '{', '}', '|', '~'])
"""

exclude = set(string.punctuation)
striptext = ''.join(char for char in filetext if char not in exclude)

lowertext = striptext.lower()

word_list = set(lowertext.split())

word_dict = dict((word, 0) for word in word_list)

for word in word_list:
	word_dict[word] = lowertext.count(word)

# for key, value in word_dict.iteritems():
#	print key, value

sorted_keys = sorted(word_dict.items(), key=itemgetter(1), reverse=True)

for key, value in sorted_keys:
	print key, value

f.close()
