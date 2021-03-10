#!/usr/bin/env python3

# www.codewars.com
# Codewars is an educational community for computer programming. On the platform, 
# software developers train on programming challenges known as kata. These discrete
# programming exercises train a range of skills in a variety of programming languages,
# and are completed within an online integrated development environment.
# On Codewars the community and challenge progression is gamified, with users
# earning ranks and honor for completing kata, contributing kata, and quality solutions.

# Exercise:
# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because
# each month a list with the weights of members is published and each month he is the last
# on the list which means he is the heaviest. I am the one who establishes the list so I told him:
# "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight"
# to numbers. The weight of a number will be from now on the sum of its digits. For example 99 will have
# "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with
# the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 
# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:
# 180 is before 90 since, having the same "weight" (9), it comes before as a string.
# All numbers in the list are positive numbers and the list can be empty.
# Notes
# it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace
# between two consecutive numbers


#--------------------------------------------------------------------------------
def order_weight(strng):

    # example_string = '9999 44444444 1234000 123 10003 22 2000 11 11' # should equal '11 11 2000 10003 22 123 1234000 44444444 9999'
    list_of_numbers = strng.split() # ['9999', '44444444', '1234000', '123', '10003', '22', '2000', '11', '11']

    # The weight of a number will be the sum of its digits, for example 99 will have "weight" 18
    list_of_numbers_and_weights = [[num, sum([int(digit) for digit in num])] for num in list_of_numbers] # [[num, weight], ['9999', 36], ...]
    sorted_list = sorted(list_of_numbers_and_weights, key=lambda x: (x[1], x[0])) # [['11', 2], ['11', 2], ['2000', 2], ['10003', 4], ['22', 4], ...]
    updated_list = [x[0] for x in sorted_list] # ['11', '11', '2000', '10003', '22', '123', '1234000', '44444444', '9999']
    updated_string = ' '.join(updated_list) # '11 11 2000 10003 22 123 1234000 44444444 9999'

    return updated_string
#--------------------------------------------------------------------------------


if __name__ == '__main__':
    strng = '9999 44444444 1234000 123 10003 22 2000 11 11' # should equal '11 11 2000 10003 22 123 1234000 44444444 9999'
    list_of_numbers = strng.split() # ['9999', '44444444', '1234000', '123', '10003', '22', '2000', '11', '11']

    # The weight of a number will be the sum of its digits, for example 99 will have "weight" 18
    list_of_numbers = strng.split() # ['9999', '44444444', '1234000', '123', '10003', '22', '2000', '11', '11']

    # The weight of a number will be the sum of its digits, for example 99 will have "weight" 18
    list_of_numbers_and_weights = [[num, sum([int(digit) for digit in num])] for num in list_of_numbers] # [[num, weight], ['9999', 36], ...]
    sorted_list = sorted(list_of_numbers_and_weights, key=lambda x: (x[1], x[0])) # [['11', 2], ['11', 2], ['2000', 2], ['10003', 4], ['22', 4], ...]
    updated_list = [x[0] for x in sorted_list] # ['11', '11', '2000', '10003', '22', '123', '1234000', '44444444', '9999']
    updated_string = ' '.join(updated_list) # '11 11 2000 10003 22 123 1234000 44444444 9999'

    # print(list_of_numbers)
    # print(list_of_numbers_and_weights)
    # print(sorted_list)
    # print(updated_list)
    # print(updated_string)