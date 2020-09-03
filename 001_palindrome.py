
# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

# Exercise 6 - String Lists
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)


def is_palindrome(user_string):

    '''\nthis function determines if a given string is a palindrome and returns True or False:
is_palindrome('hannah') -> True
is_palindrome('python') -> False
for arguments different than a string TypeError exception is raised\n'''

    if type(user_string) is not str: # function only works for strings
        raise TypeError('Only strings are allowed')

    # order of characters in a string can be reversed using [::-1] syntax
    # 'python'[::-1] -> 'nohtyp'
    # a palindrome reads the same forwards and backwards so if a string and it's reversed version are the same
    # it means that the string is a palindrome

    if user_string == user_string[::-1]:
        return True

    return False


if __name__ == '__main__':

    # ask the user for a string and print out whether this string is a palindrome or not

    user_input = input('\nEnter a string: ') # input funtion always returns a string

    if is_palindrome(user_input):  # is_palindrome returns True or False
        message_palindrome = f'\nYour string \'{user_input}\' is a palindrome.\n' # -> Your string 'hannah' is a palindrome.
        print(message_palindrome)
    else:
        message_not_palindrome = f'\nYour string \'{user_input}\' is not a palindrome.\n' # -> Your string 'python' is not a palindrome.
        print(message_not_palindrome)



