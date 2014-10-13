#!/usr/bin/env python
# Source: https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise08

"""
Description
-----------
You are to produce a random text generator using markov chains. We've provided a very bare skeleton for you to start your program from. Up until now, we've been writing our programs in a very freeform manner, just writing code at the 'top level', the same place where we put our global variables. This is generally considered bad form. Code should always be contained in functions or class methods wherever possible.

The skeleton program we've provided has a recommended set of functions to start with, including a very odd if statement at the bottom. You can ignore how this statement works for now, all it does is it makes sure your program starts inside the main() function.

The program should accept a filename from the command line, and a sample run should look similar to the following:

    python markov.py shakespeare.txt
    Forsooth, or somesuch.

You can use any text as an input corpus, you might try (Project Gutenberg) [http://www.gutenberg.org/] for some inspiration.
"""

import sys
from sys import argv
import random
import string

"""Takes an input text as a string and returns a dictionary of markov chains."""

def make_chains(corpus):

    """
    Replace "-" with " "
    e.g. "epochs--and", "smiled--not", "suppose--or", etc
    """

    corpus = corpus.replace('-',' ')

    """
    Exclude punctuation

    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python

    """

    striptext = corpus.translate(string.maketrans("",""), string.punctuation)

    word_list = striptext.lower().split()

    word_dict = {}
    word_next = []

    # { ("hello", "my"): ["name", "friend", "favorite"] }

    for index in range(len(word_list)-2):

        key = (word_list[index], word_list[index + 1])
        val = word_list[index + 2]

        if key in word_dict:
            word_dict[key].append(val)
        else:
            word_dict[key] = [val] 

    return word_dict

"""Takes a dictionary of markov chains and returns random text
    based off an original text."""

def make_text(word_dict):

    markov_text = ""

    while len(markov_text) < 100:

        random_key = random.choice(word_dict.keys())
        random_val = random.choice(word_dict[random_key])   

        markov_text += str(random_key) + " " + random_val + " "

        final_text = markov_text.translate(string.maketrans("",""), string.punctuation)

    return final_text


def main():

    script, filename = argv

    f = open(filename)
    corpus = f.read()

    word_dict = make_chains(corpus)

    print make_text(word_dict)

if __name__ == "__main__":

    main()
