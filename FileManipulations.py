# write a Python program to read a file and count the number of occurrences of each word in the file
# use a dict, indexed by word, to count the occurrences
# if your dict is d, then d.get(key) will return None if there is no such key in the dict (d[key] will throw an exception)
# your program should treat 'The' and 'the' as the same word for counting purposes
# print out the words and their counts, from least common to most common

count = {}

# filename = input('Enter a filename: ')
filename = '/tmp/poem.txt'

for line in open(filename):
    line = line.lower()
    for word in line.split():
        if count.get(word):
            count[word] += 1
        else:
            count[word] = 1

for key in sorted(count, key=count.get):
    print(key, count[key])


