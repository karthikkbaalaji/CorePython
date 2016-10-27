# write a Python program which prompts the user for a
# string and a stride (increment), and alternately makes the
# string upper case and lower case, stride characters at a
# time, e.g.,

from __future__ import print_function
print("Enter a string: ",end='')
inputString = raw_input()
print("Enter a stride(integer): ",end='')
stride = int(raw_input())
# num = stride
# for char in inputString:
#     if inputString.index(char) != num-1:
#         print(char,end='')
#         continue
#     else:
#         print(char.swapcase(),end = '')
#     num += stride

up = True
t = ''
for i in range(0,len(inputString),stride):
    if up:
        t += inputString[i:i + stride].upper()
        up = False
    else:
        t += inputString[i:i + stride].lower()
        up = True
print(t)
