# write a Python program which takes two command line arguments, a filename and a regex pattern
# your program should act like grep in that it should search for the pattern in each line of the file
# if the pattern matches a given line, print out the line

from __future__ import print_function

import sys
import re

for line in open(sys.argv[1],'r'):
    if(re.search(sys.argv[2],line)):
        print (line,end='')