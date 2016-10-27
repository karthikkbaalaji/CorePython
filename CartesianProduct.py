# 1. Start with Cartesian product example (colors x sizes of t- shirts) and add a third list, s
# leeves = ['short', 'long']
# then write a new listcomp which generates the Cartesian product colors x sizes x sleeves.
#
# 2. Use a list comprehension to create a list of the squares of the integers from 1 to 25 (i.e, 1, 4, 9, 16, ..., 625)

from __future__ import print_function

colors = ['black','white']
sizes = ['s','m','l']
sleeves = ['short','long']

tshirts = [[color,size,sleeve]  for color in colors
                                for size in sizes
                                for sleeve in sleeves]
print(tshirts,end="\n")

#2. Squares of integers

squares = [[num*num] for num in range(1,100)]
print(squares)

