#!/usr/bin/env python3

# statistics
# Write a function called statistics, which takes in a file name and returns a
# dictionary with the number of lines, words, and characters in the file.


# ---------------------------------------------------------------------------------------
def statistics(file):

    with open(file, 'r') as data_file:
        content = data_file.read()

    # to determine number of lines we need to split content of the file on '\n'   
    line_count = len(content.split('\n'))

    # to determine number of words we need to split content of the file on whitespace
    # this count is simplified, much more complicated logic would be needed for better accuracy
    # expressions like: 'print('file:',', 'open(file,', 'statistics(file)' are not 1 word
    word_count = len(content.split())

    # to determine number of characters we need length of the content of the file
    character_count = len(content)

    return {'lines': line_count, 'words': word_count, 'characters': character_count}
# ---------------------------------------------------------------------------------------


if __name__ == "__main__":

    # we're running statistcs for the current python file -> __file__ = '008_statistics.py'
    print('file:', __file__)
    print('statistics:', statistics(__file__))


# output:
# file: 008_statistics.py
# statistics: {'lines': 38, 'words': 168, 'characters': 1407}