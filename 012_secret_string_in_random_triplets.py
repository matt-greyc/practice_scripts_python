#!/usr/bin/env python3

# www.codewars.com
# Codewars is an educational community for computer programming. On the platform, 
# software developers train on programming challenges known as kata. These discrete
# programming exercises train a range of skills in a variety of programming languages,
# and are completed within an online integrated development environment.
# On Codewars the community and challenge progression is gamified, with users
# earning ranks and honor for completing kata, contributing kata, and quality solutions.

# Exercise:
# There is a secret string which is unknown to you. Given a collection of random triplets from the string,
# recover the original string. A triplet here is defined as a sequence of three letters such that each letter
# occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".
# As a simplification, you may assume that no letter occurs more than once in the secret string.
# You can assume nothing about the triplets given to you other than that they are valid triplets and that they
# contain sufficient information to deduce the original string. In particular, this means that the secret string
# will never contain letters that do not occur in one of the triplets given to you.
# secret = "whatisup"
# triplets = [
#   ['t','u','p'],
#   ['w','h','i'],
#   ['t','s','u'],
#   ['a','t','s'],
#   ['h','a','p'],
#   ['t','i','s'],
#   ['w','h','s']
# ]


#--------------------------------------------------------------------------------
def recoverSecret(triplets):

    secret = ''

    # you may assume that no letter occurs more than once in the secret string
    letters = set()
    # we add all letters to the 'letters' set, duplicates will be removed automatically
    for triplet in triplets: 
        for letter in triplet:
            letters.add(letter)

    # triplet here is defined as a sequence of three letters such that each letter occurs
    # somewhere before the next in the given string

    while letters:  # we iterate through letters until there are no letters left
        updated_letters = set(letters)

        for letter in letters:  # we try to find a letter that doesn't come after any other letter, it means it's the next letter in the message
            for triplet in triplets:
                if letter not in triplet:
                    continue
                else:
                    if letter != triplet[0]:  # if a letter isn't first on the list it means it can't be the next letter
                        updated_letters.discard(letter)  # we keep removing letters until there's only one left

        for letter in updated_letters:  # when we find the next letter we remove it from all lists so we can search for the next 'first' letter
            secret += letter
            letters.discard(letter)

            for triplet in triplets:
                if letter not in triplet:
                    pass
                else:
                    triplet.remove(letter)
    
    return secret
#--------------------------------------------------------------------------------


if __name__ == '__main__':

    # secret = "whatisup"
    triplets = [
    ['t','u','p'],
    ['w','h','i'],
    ['t','s','u'],
    ['a','t','s'],
    ['h','a','p'],
    ['t','i','s'],
    ['w','h','s']
    ]

    # you may assume that no letter occurs more than once in the secret string
    letters = set()
    # we add all letters to the 'letters' set, duplicates will be removed automatically
    for triplet in triplets: 
        for letter in triplet:
            letters.add(letter)

    # triplet here is defined as a sequence of three letters such that each letter occurs
    # somewhere before the next in the given string
    print(letters)
    secret = ''

    while letters:
        updated_letters = set(letters)

        for letter in letters:
            for triplet in triplets:
                if letter not in triplet:
                    continue
                else:
                    if letter != triplet[0]:
                        updated_letters.discard(letter)
                    print(letter, triplet)

        for letter in updated_letters:
            secret += letter
            letters.discard(letter)

            for triplet in triplets:
                if letter not in triplet:
                    pass
                else:
                    triplet.remove(letter)


        print(updated_letters)
        print(secret)
        print(letters)
        print(triplets)

    # for letter in letters:
    #     secret += letter

    print(secret)