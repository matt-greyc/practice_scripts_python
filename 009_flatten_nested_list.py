#!/usr/bin/env python3

# Take a nested list and return a single flattened list with all values except None.
# Write a function that accepts an arbitrarily-deep nested list-like structure and
# returns a flattened structure without any None values. For Example:
# input: [1, [2, 3, None, 4], [None, []], [[]], 5, None]
# output: [1,2,3,4,5]


# -----------------------------------------------------------------------------
def flatten(nested_list):
    check = True
    
    while check: # initial list is being flattend till there are no list elements remaining
        flattened_list = []

        for element in nested_list:

            # if element isn't a list and is not equal to None we append it to the flattened list
            if element != None and isinstance(element, list) == False:
                flattened_list.append(element)
            # if element is a list then we append all the elements in that list except None
            elif isinstance(element, list):
                for el in element:
                    if el != None:
                        flattened_list.append(el)

        nested_list = flattened_list

        # now we check if there are still list elements in the flattend list
        # if there aren't we return the list, else the new list is flattened again
        check = any([isinstance(x, list) for x in nested_list]) # True if any element in the new list is a list

    return flattened_list
# -----------------------------------------------------------------------------


if __name__ == '__main__':

    test_list = [[[[[[[[None, None, None]]]]]]], 1, [2, 3, None, 4], [None, []], [[]], 5, None, [[[[[[[]]]]]]]]
    flattened_list = flatten(test_list) # [1,2,3,4,5]
    print(flattened_list) 
    
# output:
# [1,2,3,4,5]


