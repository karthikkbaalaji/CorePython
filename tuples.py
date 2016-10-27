# Given a list of words, sort them by length of word, rather than alphabetically.
# To do this, first create a list of tuples of the form (len, word), where the first element is the length of the word.
# Next, sort the tuples.
# Finally, extract the words from the list of tuples into a new list which is now sorted by length of word.
# Try to use a list comprehension if you can.

from __future__ import print_function
import math

inputString = raw_input("Enter input string: ").split()
listOfTuples = [(len(word),word) for word in inputString]
listOfTuples.sort()
# sortedList = [words for length,words in listOfTuples]
sortedList = [t[1] for t in listOfTuples]
print(sortedList)
