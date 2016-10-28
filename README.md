# CorePython

This repository contains Core Python codes for basic python concepts.

### 1. String functions:
  - Python program which prompts the user for a string and a stride (increment), and alternately makes the string upper case and lower case, 
stride characters at a time. 

### 2. Additional String functions:
  - Program to:  
    a. Have the user enter two strings and indicate whether either string appears at the end of the other string, e.g.,"Bigelow", "low" => YES or "mart", "Minimart" => YES
    b. Extra...modify your solution for #1 so that case is ignored, i.e.,"Mart", "Minimart" => YES 

### 3. Loops:
  - a. Program to have the user enter a string, then loop through the string to generate a new string in which every character is duplicated   
      e.g., "hello" => "hheelllloo". 

### 4. Prime Numbers:
  - a. Program to Print prime numbers if number is not prime, print the number's divisors. 

### 5. Lists:  

 - Write a Python program to maintain two lists and loop until the user wants to quit:
 - Your program should offer the user the following options:  
	**a**. add an item to list 1 or 2
    **b.** remove an item from list 1 or 2 by value or index
    **c.** reverse list 1 or list 2
    **d**. display both lists
    **EXTRA:** add an option to check if lists are equal, even if contents are not in the same order (i.e, if list 1 is [3, 2,'apple', 4] and list 2 is [2, 3, 4, 'apple'],you should indicate they are the same).

### 6. Remove List Duplicates:

 - Python program to read in a list of items which may contain duplicates, and which constructs a new list which contains the elements from the original list, with the order preserved, but the duplicates removed.

### 7. Cartesian Product:

 - 1. Start with Cartesian product example (colors x sizes of t- shirts) and add a third list, sleeves = ['short', 'long']
then write a new listcomp which generates the Cartesian product colors x sizes x sleeves.
 - 2. Use a list comprehension to create a list of the squares of the integers from 1 to 25 (i.e, 1, 4, 9, 16, ..., 625)

### 8. Tuples:

 - Given a list of words, this program will sort them by length of word, rather than alphabetically.
 - To do this, we first create a list of tuples of the form (len, word), where the first element is the length of the word.
 - Next, we sort the tuples.
 - Finally, we can extract the words from the list of tuples into a new list which is now sorted by length of word.
 - We will use a list comprehension if you can.


### 9. Sets:

 - Program to use a set to find all of the unique words in the input and print them out in sorted order.
 - If the user entered "There is no there there", the program will print
 - is
 - no
 - there
 - Note that "There" and "there" will be counted as the same word.


### 10. Files:

 - 1. Program to prompt the user for a filename and then opens that file and writes the contents of this file to a new file in reverse order.
 - 2. Program to read a file and count the number of occurrences of each word in the file:
 - We use a dict, indexed by word, to count the occurrences
 - If dict is d, then d.get(key) will return None; if there is no such key in the dict (d[key] will throw an exception)
 - Treat 'The' and 'the' as the same word for counting purposes
 - Use a dict, indexed by word, to count the occurrences
 - Print out the words and their counts, from least common to most common
