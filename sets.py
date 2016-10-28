# Use a set to find all of the unique words in the input and print them out in sorted order.
# If the user entered "There is no there there", your program should print out
#   is
#   no
#   there
# Note that "There" and "there" should be counted as the same word.

from __future__ import print_function

inputString = raw_input("Enter a string: ")

list = inputString.split()
set = set(list)
sortedList = sorted(set)

# for item in sortedList:
#     print(item,end=' ')

print(sortedList)