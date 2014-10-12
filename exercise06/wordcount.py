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

def identify_words(filetext):

	"""
	Replace "-" with " "
	e.g. "epochs--and", "smiled--not", "suppose--or", etc
	"""

	filetext = filetext.replace('-',' ')

	"""
	Exclude punctuation

	set(['!', '#', '"', '%', '$', "'", '&', ')', '(', '+', '*', '-', ',', '/', '.', ';', ':', '=', '<', '?', '>', '@', '[', ']', '\\', '_', '^', '`', '{', '}', '|', '~'])
	"""

	exclude = set(string.punctuation)
	striptext = ''.join(char for char in filetext if char not in exclude)

	lowertext = striptext.lower()

	word_list = set(lowertext.split())

	return lowertext, word_list

def create_dictionary(lowertext, word_list):
	word_dict = {}

	for word in word_list:
		word_dict[word] = lowertext.count(word)

	return word_dict

def print_words(word_dict):
	
	sort_by = raw_input("> ")
	
	if sort_by == 'alpha':
		for key in sorted(word_dict.iterkeys()):
			print key, word_dict[key]
	elif sort_by == 'desc':
		sorted_keys = sorted(word_dict.items(), key=itemgetter(1), reverse=True)
		for key, value in sorted_keys:
			print key, value
	elif sort_by == 'asc':
	#	sorted(dict.iteritems(), key=lambda (k,v): (v,k))
		sorted_keys = sorted(word_dict.items(), key=itemgetter(1))
		for key, value in sorted_keys:
			print key, value

def main():

	script, filename = argv

	print "Counting words ..."

	f = open(filename)
	filetext = f.read()

	lowertext, word_list = identify_words(filetext)
	word_dict = create_dictionary(lowertext, word_list)

	print "Sort by alphabet > alpha OR Sort by count desc > desc OR Sort by count asc > asc"

	print_words(word_dict)

	f.close()

if __name__ == "__main__":
	main()	
