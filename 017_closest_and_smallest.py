#!/usr/bin/env python3

# www.codewars.com
# Codewars is an educational community for computer programming. On the platform, 
# software developers train on programming challenges known as kata. These discrete
# programming exercises train a range of skills in a variety of programming languages,
# and are completed within an online integrated development environment.
# On Codewars the community and challenge progression is gamified, with users
# earning ranks and honor for completing kata, contributing kata, and quality solutions.


# Exercise:
# Input a string strng of n positive numbers (n = 0 or n >= 2). Let us call weight of a number the sum of its digits. For example
# 99 will have "weight" 18, 100 will have "weight" 1. Two numbers are "close" if the difference of their weights is small.
# Task:
# For each number in strng calculate its "weight" and then find two numbers of strng that have: the smallest difference of weights
# ie that are the closest with the smallest weights and with the smallest indices (or ranks, numbered from 0) in strng
# Output:
# an array of two arrays, each subarray in the following format:
# [number-weight, index in strng of the corresponding number, original corresponding number in strng]
# The two subarrays are sorted in ascending order by their number weights if these weights are different,
# by their indexes in the string if they have the same weights.
# Examples:
# Let us call that function closest
# strng = "103 123 4444 99 2000"
# the weights are 4, 6, 16, 18, 2 (ie 2, 4, 6, 16, 18)
# closest should return [[2, 4, 2000], [4, 0, 103]] (or ([2, 4, 2000], [4, 0, 103])
# because 2000 and 103 have for weight 2 and 4, their indexes in strng are 4 and 0.
# The smallest difference is 2.
# 4 (for 103) and 6 (for 123) have a difference of 2 too but they are not 
# the smallest ones with a difference of 2 between their weights.

# ....................
# strng = "80 71 62 53"
# All the weights are 8.
# closest should return [[8, 0, 80], [8, 1, 71]]
# 71 and 62 have also:
# - the smallest weights (which is 8 for all)
# - the smallest difference of weights (which is 0 for all pairs)
# - but not the smallest indices in strng.
# ....................


#--------------------------------------------------------------------------------
def closest(strng):
    # strng = "456899 50 11992 176 272293 163 389128 96 290193 85 52"
    
    if not strng: # returns [] for empty strings
        return []
    
    nums_weights = []
    final_list = []
    
    nums = strng.split()  # string is split on the whitespace -> ['456899', '50', '11992', '176', '272293', '163', '389128', '96', '290193', '85', '52']
    
    for i in range(len(nums)):  # we create a list of numbers with their weights and indexes [weight, index, num] -> [14, 3, 176]
        num = nums[i]
        weight = sum(int(digit) for digit in num)
        nums_weights.append([weight, i, int(num)])      

    while len(nums_weights) > 1:    # we compare all elements to each other to get their weight difference
        element = nums_weights[0]

        for x in nums_weights[1:]:  #  first element on the list is compared to all the other elements
            weigth_difference = abs(element[0] - x[0])
            final_list.append([weigth_difference, sorted([element, x], key=lambda y: y[1])])  # -> [3, [[10, 5, 163], [13, 9, 85]]]

        nums_weights = nums_weights[1:]  #  first element is removed from the list before next loop

    final_list_sorted = sorted(final_list)  # final list is sorted by weight difference
    final_result = final_list_sorted[0]  # we get the first element on the final list -> [1, [[14, 3, 176], [13, 9, 85]]]
    final_result = sorted([final_result[1][0], final_result[1][1]])  # -> [[13, 9, 85], [14, 3, 176]]

    return final_result
#--------------------------------------------------------------------------------


if __name__ == '__main__':
    strng = "456899 50 11992 176 272293 163 389128 96 290193 85 52"
    # closest("456899 50 11992 176 272293 163 389128 96 290193 85 52")  should return  [[13, 9, 85], [14, 3, 176]])
    nums = strng.split()
    # print(nums)
    nums_weights = []
    final_list = []

    for i in range(len(nums)):
        num = nums[i]
        nums_weights.append([sum(int(digit) for digit in num), i, int(num)])

    # print(nums_weights)    

    while len(nums_weights)>1:
        element = nums_weights[0]

        for x in nums_weights[1:]:
            weigth_difference = abs(element[0] - x[0])
            final_list.append([weigth_difference, sorted([element, x], key=lambda y: y[1])])

        nums_weights = nums_weights[1:]

    # print(final_list)
    final_list_sorted = sorted(final_list)
    final_result = final_list_sorted[0]
    # print(final_result)
    final_result = sorted([final_result[1][0], final_result[1][1]])

    print(final_result)
    print(closest(strng))
    print(final_result == closest(strng))