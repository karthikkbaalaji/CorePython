# write a Python program which prompts the user for a filename,
# then opens that file and writes the contents of the file to a new file, in reverse order

with open('/tmp/text.txt','r') as f1:
    lines = f1.readlines()
with open('/tmp/test2.txt','w') as f2:
    for line in reversed(lines):
        f2.write(line)
f2.close()
f1.close()