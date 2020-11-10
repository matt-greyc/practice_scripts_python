#!/usr/bin/env python3


# Write a function that accepts a string and returns a dictionary with the keys
# as the vowels and values as the count of that vowel in the string.
# fn('Python Is Awesome') -> {'a': 1, 'e': 2, 'i': 1, 'o': 2}

# -------------------------------------------------------------------------------
def vowel_count_dict(string=''):

    vowels = 'aeiou'

    string = string.lower() # we're converting uppercase to lowercase

    # now we use dictionary comprehension to create required dict
    dict_vowel_count = {letter:string.count(letter) for letter in string if letter in vowels}

    return dict_vowel_count
# -------------------------------------------------------------------------------


# Write a function that reverses the order of vowels in a string,
# other characters should remain in their original position.
# fn('Matthew')) -> 'Metthaw'

# -------------------------------------------------------------------------------
def reversed_vowels(string=''):

    vowels = 'aeiou'
    # we're not igoring uppercase so we have to include uppercase vowels
    vowels += vowels.upper() # 'aeiouAEIOU' 
    
    # we create a list of vowels in a string
    list_of_vowels = [letter for letter in string if letter in vowels]

    # now we're swapping the order of vowels in the original string
    new_string = []
    for letter in string:
        if letter not in vowels:
            new_string.append(letter)
        else:
            new_string.append(list_of_vowels.pop(-1)) # we're appending vowels in a reverse order

    return ''.join(new_string)
# -------------------------------------------------------------------------------


if __name__ == '__main__':

    test_string = 'Python Is Awesome'

    print(vowel_count_dict(test_string)) # {'o': 2, 'i': 1, 'a': 1, 'e': 2}
    print(vowel_count_dict('Matthew')) # {'a': 1, 'e': 1}
    print(vowel_count_dict('aeiouAEIOU')) # {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}

    print(reversed_vowels(test_string)) # Pythen os ewAsImo
    print(reversed_vowels('Matthew')) # Metthaw
    print(reversed_vowels('aeiouAEIOU')) # UOIEAuoiea



