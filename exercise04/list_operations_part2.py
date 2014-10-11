"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""

def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    i = 0
    for input in input_list:
        i += 1
    return i

def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
    input_list[custom_len(input_list):] = [value]

def custom_extend(input_list, values):
    """custom_extend(input_list, values) imitates input_list.extend(values)"""
    input_list[custom_len(input_list):] = values

def custom_insert(input_list, index, value):
    """custom_insert(input_list, index, value) imitates
    input_list.insert(index, value)
    """
    input_list[index:index] = [value]

def custom_remove(input_list, value):
    """custom_remove(input_list, value) imitates input_list.remove(value)"""
    index = custom_index(input_list, value)
    del input_list[index]

def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    pop = input_list[-1]
    del input_list[-1]
    return pop

def custom_index(input_list, value):
    """custom_index(input_list, value) imitates input_list.index(value)"""
    index = 0
    for i in range(0, custom_len(input_list)):
        if input_list[i] == value:
            index = i
            break
    return index

def custom_count(input_list, value):
    """custom_count(input_list, value) imitates input_list.count(value)"""
    i = 0
    for input in input_list:
        if input == value:
            i += 1
    return i

def custom_reverse(input_list):
    """custom_reverse(input_list) imitates input_list.reverse()"""
    new_list = input_list[::-1]
    input_list[:] = new_list

def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""
    for input in input_list:
        if input == value:
            return True
    return False

def custom_equality(some_list, another_list):
    """custom_equality(some_list, another_list) imitates
    (some_list == another_list)
    """
    if custom_len(some_list) != custom_len(another_list):
        return False
    else:
        for i in range(0, custom_len(some_list)):
            if some_list[i] != another_list[i]:
                return False
        return True
