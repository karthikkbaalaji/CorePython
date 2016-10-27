# Write a Python program to read in a list of items which may contain duplicates, and which
# constructs a new list which contains the elements from the original list,
# with the order preserved, but the duplicates removed

from __future__ import print_function

print("Enter the list values separated by commas: ", end = '')
list = raw_input().split(',')
list2 = []

for items in list:
    if not items in list2:
        list2.append(items)
print("Uniqe list:",list2)
print(','.join(list2))
