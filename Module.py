import Calculator
# from Calculator import calculator


x,operand,y = raw_input('Enter x operand y(Eg, 5 * 10) :').split(' ')
print(Calculator.calculator(int(x),int(y),operand))

