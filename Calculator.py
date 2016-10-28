#turn your calculate() function into a standalone program
# which takes 3 command line arguments and invokes calculate() with those arguments

from __future__ import print_function
import sys

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

# print(sys.argv)
# print(calculator(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]))