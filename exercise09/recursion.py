# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] * multiply_list(l[1:])

print multiply_list([1, 2, 3])

# Return the factorial of n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(0)
print factorial(4)

# Count the number of elements in the list l
def count_list(l):
    if len(l) == 1:
        return 1
    else:
        return 1 + count_list(l[1:])

print count_list([1])
print count_list([1, 2, 3, 4, 5])

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sum_list(l[1:])

print sum_list([2])
print sum_list([1, 2, 3, 4])

# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return [l[0]]
    else:
        return [l[-1]] + reverse(l[:-1])

print reverse([1, 2, 3, 4])

# Fibonacci returns the nth fibonacci number. 
# The nth fibonacci number is defined as fib(n) = fib(n-1) + fib(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(4)
print fibonacci(5)
print fibonacci(6)
print fibonacci(7)
print fibonacci(8)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l[0] == i:
        return 0
    else:
        return 1 + find(l[1:], i)

print find([0, 1, 2, 3], 2)

# Determines if a string is a palindrome
def palindrome(some_string):
    if len(some_string) == 1:
        return True
    else:
        return some_string[0] == some_string[-1] and palindrome(some_string[1:-1])

print palindrome("mari")
print palindrome("aya")

# Given the width and height of a sheet of paper, 
# and the number of times to fold it, 
# return the final dimensions of the sheet as a tuple. 
# Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    pass

# Count up
# Print all the numbers from n to target
def count_up(target, n):
    if n == target:
        return target
    else:
        print n
        return count_up(target, n+1)

print count_up(10, 4)
print count_up(10, 10)