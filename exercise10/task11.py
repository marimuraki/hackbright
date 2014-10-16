#!/bin/env python

"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""

def title(title):
	
	exceptions = ['a', 'an', 'at', 'in', 'is', 'from', 'of', 'to', 'the', 'with']
	
	word_list = title.split()
    title_words = [word_list[0].capitalize()]
    for word in word_list[1:]:
    	title_words.append((word in exceptions and word) or word.capitalize()) # word in exceptions -> [True, False, ...]
    return " ".join(title_words)

# from titlecase import titlecase
