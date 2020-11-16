#!/usr/bin/env python3

# Exercise:
# Define a class with a generator which can iterate the numbers, which are
# divisible by 7, between a given range 0 and n.

class CustomRangeSeven:

    # ------------------------------------------------------------------
    def __init__(self, end_of_range):

        try: # if entered value isn't numeric program will crash
            if end_of_range >= 0 and int(end_of_range) == float(end_of_range):
                # end_of_range >= 0 -> number is positive
                # int(end_of_range) == float(end_of_range) -> number is a whole number, eg. 105.0 = 105
                self.end_of_range = end_of_range
            else:
                raise ValueError('Only positive, whole numbers are allowed.') # for negative numbers and floats
        except:
            raise ValueError('Only positive, whole numbers are allowed.') # if value is not numeric
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    def __iter__(self):

        count = 0

        while count <= self.end_of_range: # loop is exhausted when it hits end of range
            
            if count % 7 == 0: # returns a value if it's divisible by 7
                yield count # we use 'yield' keyword to create a generator expression

            count += 1 # with each loop iteration count is increased by one
    # ------------------------------------------------------------------


if __name__ == '__main__':

    for num in CustomRangeSeven(77.0): # works for both 77 and 77.0
        print(num)

# output:
# 0
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70
# 77



