# 1. Write a function calculate which is passed two operands and an operator and returns the calculated result,
# e.g. calculate(2, 4, '+') would return 6
# 2. Write a function which takes an integer as a parameter, and sums up its digits.
# If the resulting sum contains more than 1 digit, the function should sum the digits again,
# e.g., sumdigits(1235) should compute the sum of 1, 2, 3, and 5 (11), then compute the sum of 1 and 1, returning 2.
# 3. Write a function which takes a number as a parameter and returns a string version of the number with commas
# representing thousands, e.g., add_commas(12345) would return "12,345"

from __future__ import print_function
import math


def calculator(x,y,operand,**kwargs):

    # for key in kwargs:
    if(kwargs.get('float')==True):
        x = float(x)
        y = float(y)
    if(operand == '+'):
        return x + y
    elif(operand == '-'):
        return x - y
    elif(operand == '/'):
        try:
            return x / y
        except ZeroDivisionError as e:
            #gives the name of the exception
            return('Invalid division',type(e).__name__)
    elif(operand == '*'):
        return x * y
    else:
        return ('Invalid operand passed')

def sumTheDigits(x):
    sum = 0
    for digit in x:
        sum = sum + int(digit)
    return sum

def formattedNumber(x):
    position = 0
    number = ''
    for digit in reversed(x):
        if(position % 3 != 0):
            number = number + digit
        else:
            number = number + ',' + digit
        position = position + 1
    number = number[::-1]
    return number[0:len(number)-1]

x,operand,y = raw_input('Enter x operand y(Eg, 5 * 10) :').split(' ')
print(calculator(int(x),int(y),operand))

x = raw_input('Enter a number to find digits sum :')
print(sumTheDigits(x))

x = raw_input('Enter a number to be formatted :')
print(formattedNumber(x))

print(calculator(1,2,'*',float=True))