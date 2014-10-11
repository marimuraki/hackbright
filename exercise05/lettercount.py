# Source: https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise05

"""
Problem Description
-------------------
Write a program, lettercount.py, that opens a file named on the command line and counts how many times each letter occurs in that file. Your program should then print those counts to the screen, in alphabetical order.
       
 """

 # Modification: 	Creating dictionary and printing key, value
 # 					instead of only printing counts

from sys import argv
import string

script, filename = argv

f = open(filename)
filetext = f.read()
lowertext = filetext.lower()

alphabet = list(string.ascii_lowercase)

alphabet_dict = {}

for letter in alphabet:
	alphabet_dict[letter] = lowertext.count(letter)

for key, value in alphabet_dict.iteritems():
	print key, value

f.close()
