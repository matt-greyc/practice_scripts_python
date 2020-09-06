#!/usr/bin/env python3

# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

# Exercise 23 - File Overlap  
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of
# happy numbers up to 1000. (Prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.)


# --------------------------------------------------------------------
def get_file_content(file): # this function returns content of a file

    with open(file, 'r') as data_file:
        content = data_file.read()
    
    return content
# --------------------------------------------------------------------


if __name__ == '__main__':
    
    file_1 = '002_file_overlap_happy_numbers.txt'
    file_2 = '002_file_overlap_prime_numbers.txt'

    # content is assigned to a variable
    content_file_1 = get_file_content(file_1) # content of the 1st file, e.g. -> '1 2 3 4 5'
    content_file_2 = get_file_content(file_2) # content of the 2nd file, e.g. -> '3 4 5 6 7'

    # we split the content to get numbers
    nums_file_1 = content_file_1.split() # splits the content on whitespace -> ['1', '2', '3', '4', '5']
    nums_file_2 = content_file_2.split() # splits the content on whitespace -> ['3', '4', '5', '6', '7']

    # now we convert lists of numbers into sets, duplicates are removed if they are present
    set_nums_file_1 = set(nums_file_1) # list to set conversion -> {'5', '2', '1', '4', '3'}
    set_nums_file_2 = set(nums_file_2) # list to set conversion -> {'5', '7', '6', '4', '3'}
 
    # we find overlapping numbers using set intersection method -> set.intersection(set1, set2 ... etc)
    # intersection() method returns a new set with elements that are common to all sets
    overlapping_numbers = set_nums_file_1.intersection(set_nums_file_2) # -> {'3', '5', '4'}

    print(overlapping_numbers)