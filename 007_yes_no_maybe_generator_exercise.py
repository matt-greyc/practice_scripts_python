#!/usr/bin/env python3

# exercise:
# Write a function called yes_no_maybe, which returns a generator that first yields
# yes, then no, then maybe, then yes, then no, they maybe and so on.


# ---------------------------------------------------------------------------------
def yes_no_maybe():

    answers = ('yes', 'no', 'maybe')
    answer_index = 0
    last_index = len(answers) - 1 # last index in the answers tuple

    while True: # while loop will create inexhaustible generator

        yield answers[answer_index]  # returns one of the choices 'yes', 'no' or 'maybe'
        answer_index += 1  # we increase the index to get the next value
        
        if answer_index > last_index:  # when we reach the end of the tuple index is reset to 0
            answer_index = 0
# ---------------------------------------------------------------------------------


if __name__ == '__main__':

    choice = yes_no_maybe()

    for i in range(10):
        print(i+1, next(choice))


# output:
# 1 yes
# 2 no
# 3 maybe
# 4 yes
# 5 no
# 6 maybe
# 7 yes
# 8 no
# 9 maybe
# 10 yes

