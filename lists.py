#write a Python program to maintain two lists and loop
#until the user wants to quit
#your program should offer the user the following options:
#   add an item to list 1 or 2
#   remove an item from list 1 or 2 by value or index
#   reverse list 1 or list 2
#   display both lists
#EXTRA: add an option to check if lists are equal, even if
#contents are not in the same order (i.e, if list 1 is [3, 2,
#'apple', 4] and list 2 is [2, 3, 4, 'apple'], you
#should indicate they are the same)


from __future__ import print_function

lists = [[],[]]

while True:
    print('''Choose your option:
    a. Add item to a list
    b. Remove an item from a list by index
    c. Remove an item from a list by value
    r. Reverse the list
    f. Check if both lists are equal
    d. Display both lists
    e. Exit''')
    option = raw_input()

    #option to add item to the list
    if option == 'a':
        print("Enter which list to add item(1-2): ")
        num = int(raw_input())
        print("Enter the item: ")
        item = raw_input()
        lists[num-1].append(item)
        print("Item added ")

    #Removing item from list using item index
    if option == 'b':
        print("Enter which list to remove item(1-2): ")
        num = int(raw_input())
        print("Enter the item index: ")
        item = int(raw_input())
        lists[num-1].pop(item)

    #Removing item from list using item value
    if option == 'c':
        print("Enter which list to remove item(1-2): ")
        num = int(raw_input())
        print("Enter the item value: ")
        item = raw_input()
        lists[num-1].remove(item)

    #Reversing a list
    if option == 'r':
        print("Enter which list to reverse(1-2): ")
        num = int(raw_input())
        lists[num-1] = lists[num-1][::-1]
        #lists[num-1].reverse()

    #Comparing lists
    if option == 'f':
        for i in range(0,2):
            print("List", i+1 , lists[i])
        if(sorted(lists[0]) == sorted(lists[1])):
            print("Lists are equal")
        else:
            print("Lists are not equal")

    #Display lists
    if option == 'd':
        for i in range(0,2):
            print("List", i+1 , lists[i])

    #Exit
    if option == 'e':
        break

    else:
        print("Incorrect Option!")