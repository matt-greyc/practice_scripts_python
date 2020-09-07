#!/usr/bin/env python3

# Colt Steele - The Modern Python 3 Bootcamp (Udemy online learning platform) 

# coding exercise: list_check
# Write a function which accepts a list and returns True if each value in the list is a list.
# Otherwise the function should return False.


def list_check(test_list):

    if type(test_list) is not list: # function only works for list
        raise TypeError('Only lists are allowed')

    if not test_list: # if test_list is empty function will return False, same as if test_list == []
        return False

    # all() method returns True when all elements in the given iterable are true. If not, it returns False

    check = [type(element) is list for element in test_list] # (type(element) is list) evaluates to True or False

    if all(check): # True if every element in a list is a list
        return True
    
    return False


if __name__ == '__main__':
    test_list_true = [[4], [], [1], [True], [2,3], [1,3], [(5,2)]] # True
    test_list_false = [4, [], [1], True, [2,3], [1,3], (5,2)] # False
    empty_list = [] # False

    print(list_check(test_list_true)) # True
    print(list_check(test_list_false)) # False
    print(list_check(empty_list)) # False
    print(list_check([5])) # False
    print(list_check(['False'])) # False
    print(list_check([[]])) # True
    print(list_check(5)) # TypeError is raised
