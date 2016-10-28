# write a Python program which prompts the user for a filename,
# then opens that file and writes the contents of the file to a new file, in reverse order

with open('/tmp/text.txt','r') as f1:
    lines = f1.readlines()
with open('/tmp/test2.txt','w') as f2:
    for line in reversed(lines):
        f2.write(line)
f2.close()
f1.close()

# write a Python program to read a file and count the number of occurrences of each word in the file
# use a dict, indexed by word, to count the occurrences
# if your dict is d, then d.get(key) will return None if there is no such key in the dict (d[key] will throw an exception)
# your program should treat 'The' and 'the' as the same word for counting purposes
# print out the words and their counts, from least common to most common
# Road Not Taken and Hamlet are available at   https://github.com/davewadestein/Python-Core

