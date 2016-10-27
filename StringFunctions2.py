# 1. Have the user enter two strings and indicate whether
# either string appears at the end of the other string, e.g.,
# "Bigelow", "low" => YES
# "mart", "Minimart" => YES
# 2. Extra...modify your solution for #1 so that case is
# ignored, i.e.,
# "Mart", "Minimart" => YES

from __future__ import print_function

string1 = raw_input("Enter string1: ").lower()
string2 = raw_input("Enter string2: ").lower()

len1 = len(string1)
len2 = len(string2)

if(string1[-len2:] == string2):
    print("\"",string1,"\",\"",string2 ,"\" => YES")
elif(string2[-len1:] == string1):
    print("\"", string1, "\",\"", string2, "\" => YES")
