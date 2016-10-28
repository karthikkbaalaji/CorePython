# write a Python program to read a file and count the number of occurrences of each word in the file
# use a dict, indexed by word, to count the occurrences
# if your dict is d, then d.get(key) will return None if there is no such key in the dict (d[key] will throw an exception)
# your program should treat 'The' and 'the' as the same word for counting purposes
# print out the words and their counts, from least common to most common

import string

#filename = input('Enter a filename: ')
filename = '/tmp/poem.txt'
ex = set(string.punctuation)
count = {}

for line in open(filename):
    line = line.lower()
    line = ''.join([ch for ch in line if ch not in ex])
    for word in line.split():
        count[word] = count.get(word, 0) + 1

for key in sorted(count, key=count.get):
    print(key, count[key])



