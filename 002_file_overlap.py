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
    
    file1 = '002_file_overlap_happy_numbers.txt'
    file2 = '002_file_overlap_prime_numbers.txt'

    file1_content = get_file_content(file1)
    file2_content = get_file_content(file2)

    file1_nums = set(file1_content.split())
    file2_nums = set(file2_content.split())
    
    overlapping_numbers = file1_nums.intersection(file2_nums)

    print(overlapping_numbers)