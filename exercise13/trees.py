#!/usr/bin/env python

"""
TODO: FIX

Case 1:

*[master][~/Dropbox/Mari/courses/Hackbright/exercise13]$ python trees.py "5 * (5 / 6)"
5 * (5 / 6)
5.0

*[master][~/Dropbox/Mari/courses/Hackbright/exercise13]$ python trees.py "(5 * (5 / 6))"
(5 * (5 / 6))
4.16666666667

Case 2:

*[master][~/Dropbox/Mari/courses/Hackbright/exercise13]$ python trees.py "5 * (5 / 6)"
(5 * (5 / 6))
4.16666666667

*[master][~/Dropbox/Mari/courses/Hackbright/exercise13]$ python trees.py "(5 * (5 / 6))"
((5 * (5 / 6)))
None

"""

from sys import argv

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tokenize(string):
    return string.replace("(", " ( ").replace(")", " ) ").split()

def build_parse_tree(token_list):
    """Takes in a token list and produces a parse tree according to the rules in the README"""
    """Create an empty node.
    While there are tokens remaining, consume a token from the available input.

    1. If that token is a '(', call build_parse_tree on the remaining input,
    and assign the results of that to the left side of your current node.

    2. If the token is an operator + - / *, set the current node's value to
    that operator, then call build_parse_tree on the remaining input and assign
    the result of that to the right side of your current node.

    3. If the token is a number, set the value of the current node to the
    number (converting it from a string) and return that node.

    4. If the token is a ')', return the current node."""

    node = BinaryTreeNode(None)
    while token_list:
        current = token_list.pop(0)
        if current == "(":
            node.left = build_parse_tree(token_list)
        elif current in ("+", "-", "*", "/"):
            node.value = current
            node.right = build_parse_tree(token_list)
        elif is_num(current) == True:
            node.value = float(current)
            return node
        elif current == ")":
            return node

def is_num(string):
    try:
        float(string)
        return True
    except:
        return False

def evaluate_tree(node):
    if node is None:
        return
    if type(node.value) == float:
        return node.value
    elif node.value == "+":
        return evaluate_tree(node.left) + evaluate_tree(node.right)
    elif node.value == "*":
        return evaluate_tree(node.left) * evaluate_tree(node.right)
    elif node.value == "/":
        return evaluate_tree(node.left) / evaluate_tree(node.right)
    elif node.value == "-":
        return evaluate_tree(node.left) - evaluate_tree(node.right)

def main():

    script, input = argv

    equation = "(" + input + ")"
    print equation

    tokens = tokenize(equation)
    tree = build_parse_tree(tokens)
    print evaluate_tree(tree)

if __name__ == "__main__":
    main()
