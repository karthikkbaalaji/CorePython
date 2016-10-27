#  Have the user enter a string, then loop through the
# string to generate a new string in which every character
# is duplicated, e.g., "hello" => "hheelllloo"

#import print function from python3
from __future__ import print_function

#get the input from the user
print("Enter a string:", end='')
inputString = raw_input()

#print as required
for letter in inputString:
    print(letter*2, end='')