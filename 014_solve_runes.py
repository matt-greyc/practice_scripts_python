#!/usr/bin/env python3

# www.codewars.com
# Codewars is an educational community for computer programming. On the platform, 
# software developers train on programming challenges known as kata. These discrete
# programming exercises train a range of skills in a variety of programming languages,
# and are completed within an online integrated development environment.
# On Codewars the community and challenge progression is gamified, with users
# earning ranks and honor for completing kata, contributing kata, and quality solutions.

# Exercise:
# You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system,
# and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators,
# but he needs your help to figure out the rest. The professor will give you a simple math expression, of the form
# [number][op][number]=[number]
# He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-),
# and multiplication (*), so those are the only ones that will appear. Each number will be in the range from -1000000 to 1000000,
# and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s. If there are ?s in an expression,
# they represent a digit rune that the professor doesn't know (never an operator, and never a leading -). All of the ?s
# in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression.
# No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.
# Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works,
# give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong.
# output -1 in that case. Complete the method to solve the expression to find the value of the unknown rune.
# The method takes a string as a paramater representing the expression and will return an int value representing the unknown rune
# or -1 if no such rune exists.

# solve_runes("1+1=?"), 2, "Answer for expression '1+1=?'
# solve_runes("123*45?=5?088"), 6, "Answer for expression '123*45?=5?088' 
# solve_runes("-5?*-1=5?"), 0, "Answer for expression '-5?*-1=5?' 
# solve_runes("19--45=5?"), -1, "Answer for expression '19--45=5?' 
# solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?'
# solve_runes("?*11=??"), 2, "Answer for expression '?*11=??'
# solve_runes("??*1=??"), 2, "Answer for expression '??*11=??' 


#--------------------------------------------------------------------------------
def solve_runes(expression):

    values = list('1234567890')

    # expression = '-5?*-1=5?'
    expression = expression.replace('=', '==') # we replace '=' with '==' so we can use eval() 

    # All of the ?s in an expression will represent the same digit (0-9),
    # and it won't be one of the other given digits in the expression
    allowed_values = [value for value in values if value not in expression]

    # No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.
    if '0' in allowed_values and '??' in expression:
        allowed_values.remove('0')

    solutions = []

    for value in allowed_values:
        new_expression = expression.replace('?', value) # '-5?*-1=5?' becomes '-52*-1=52'

        try:
            evaluated_expression = eval(new_expression) # eval('-52*-1=52') returns True or False
        except SyntaxError:
            continue

        if evaluated_expression == True:  # if number is correct we add it to the list of solutions
            solutions.append(value)
    
    if not solutions:
        return -1

    return min([int(num) for num in solutions])  # we return the lowest number in the list of solutions
#--------------------------------------------------------------------------------


if __name__ == '__main__':

    values = list('1234567890')
    print(values)
 
    expression = "1+1=?"
    # expression = "-5?*-1=5?"
    expression = expression.replace('=', '==')

    # All of the ?s in an expression will represent the same digit (0-9),
    # and it won't be one of the other given digits in the expression

    allowed_values = [value for value in values if value not in expression]

    if '0' in allowed_values and '??' in expression:
        allowed_values.remove('0')

    print(allowed_values)

    solutions = set()

    for value in allowed_values:
        new_expression = expression.replace('?', value)
        evaluated_expression = eval(new_expression)
        print(value, new_expression, evaluated_expression)
        if evaluated_expression == True:
            solutions.add(value)

    print(solutions)
    print('solution', min(solutions))

