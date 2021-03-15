#!/usr/bin/env python3

# www.codewars.com
# Codewars is an educational community for computer programming. On the platform, 
# software developers train on programming challenges known as kata. These discrete
# programming exercises train a range of skills in a variety of programming languages,
# and are completed within an online integrated development environment.
# On Codewars the community and challenge progression is gamified, with users
# earning ranks and honor for completing kata, contributing kata, and quality solutions.

# Exercise:
# Create two functions to encode and then decode a string using the Rail Fence Cipher.
# This cipher is used to encode a string by placing each character successively in a diagonal
# along a set of "rails". First start off moving diagonally and down. When you reach the bottom,
# reverse direction and move diagonally and up until you reach the top rail. Continue until you
# reach the end of the string. Each "rail" is then read left to right to derive the encoded string.
# For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

# W       E       C       R       L       T       E
#   E   R   D   S   O   E   E   F   E   A   O   C  
#     A       I       V       D       E       N

# The encoded string would be: WECRLTEERDSOEEFEAOCAIVDEN
# Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.
# Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns
# the DECODED string. For both encoding and decoding, assume number of rails >= 2 and that passing an empty string
# will return an empty string. Note that the example above excludes the punctuation and spaces just for simplicity.
# There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.


#--------------------------------------------------------------------------------
def encode_rail_fence_cipher(string, n):
    # n = 3
    # string = 'HAMSTER'
    rails = []
    current_rail = 0

    for i in range(n):  
        rails.append('')  # we create a list of empty rails -> ['', '', '']

    for char in string:

        rails[current_rail] += char  #  we add letter to the current rail

        if current_rail == 0: # we keep adding letters to the next rail until we reach the 'bottom' rail
            step = 1
        elif current_rail == len(rails) -1:  # when we hit the last rail we reverse the direction
            step = -1

        current_rail += step  #  we switch between rails in 0,1,2,1,0,1,2 pattern (example case has 3 rails)

    return ''.join(rails)   #  we return string version of the rails list: ['HT', 'ASE', 'MR'] -> 'HTASEMR'
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------    
def decode_rail_fence_cipher(string, n):
    # n = 3
    # string = 'HTASEMR'
    rails = []
    current_rail = 0

    for i in range(n):
        rails.append('')  # we create a list of empty rails -> ['', '', '']

    for num in range(len(string)):

        rails[current_rail] += f'i{num}'  #  we create a list of indexes that we'll use to decode the string -> ['i0i4', 'i1i3i5', 'i2i6'] 

        if current_rail == 0:  # we keep adding indexes to the next rail until we reach the 'bottom' rail
            step = 1
        elif current_rail == len(rails) -1:  # when we hit the last rail we reverse the direction
            step = -1

        current_rail += step  #  we switch between rails in 0,1,2,1,0,1,2 pattern (example case has 3 rails)

    indexes = ''.join(rails)  #  ['i0i4', 'i1i3i5', 'i2i6']  ->  'i0i4i1i3i5i2i6'
    #  we split indexes on the letter 'i' and get rid of empty strings: 'i0i4i1i3i5i2i6'  ->  ['0', '4', '1', '3', '5', '2', '6']
    indexes = [i for i in indexes.split('i') if i]
    # we zip encoded string with the list of indexes:  [(0, 'H'), (4, 'T'), (1, 'A'), (3, 'S'), (5, 'E'), (2, 'M'), (6, 'R')]
    zipped_data = [(int(x[0]), x[1]) for x in zip(indexes, list(string))] 
    #  we sort zipped list by index number ->  [(0, 'H'), (1, 'A'), (2, 'M'), (3, 'S'), (4, 'T'), (5, 'E'), (6, 'R')]
    zipped_data = sorted(zipped_data)
    # we join sorted letters to create the decoded string: [(0, 'H'), (1, 'A'), (2, 'M'), (3, 'S'), (4, 'T'), (5, 'E'), (6, 'R')] -> 'HAMSTER'
    decoded_string = ''.join([x[1] for x in zipped_data])

    return decoded_string
#--------------------------------------------------------------------------------
