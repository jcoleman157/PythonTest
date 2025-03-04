"""
Author: Jacob Coleman
This is program takes 2 .list files and returns what files are "crossed"
You can take the path beforehand to optomize it (e.g. /user, /ect)

I have used line by line file checking in the past trying to combat rubber ducky attacks
unfortunetly I have never finished the rubber ducky project but I am trying to find time to work on it
"""

import re
system_arr_1 = []
system_arr_2 = []
together = []

print("Dont forget the .list extention!")

sys1 = open(input("What is the path to the first file (if its in this directory just say the file name) "), encoding='utf-8', errors='ignore')
sys2 = open(input("What is the path to the second file (if its in this directory just say the file name) "), encoding='utf-8', errors='ignore')
path = input("What path do you want to check for (leave blank for all files) ")


# This is the cross file checker, allows for cross checking files
def cross_file_checker():
    search_path = r" " + path

    for i in sys1.readlines():
        searched = re.search(search_path, i)
        if searched:
            system_arr_1.append(i[i.index(" ") + 2:])
    
    for i in sys2.readlines():
        searched = re.search(search_path, i)
        if searched:
            system_arr_2.append(i[i.index(" ") + 2:])
    NOT_SAME_NAME1()
    NOT_SAME_NAME2()
    # SAME_NAME()



# This will print out "x is not on system 1... y is not on system 2"
def NOT_SAME_NAME1():
    reject = []
    for i in system_arr_1:
        temp = ""
        count = 0
        for x in system_arr_2:
            temp = x
            if x == i:
                print("Made it in here 1")
                count = 1
                break
        if temp == None:
            print("Made it in here 2")
            break
        if count == 1:
            continue
        reject.append(temp)
    for y in reject:
        print(y)



def NOT_SAME_NAME2():
    reject = []
    for i in system_arr_2:
        temp = ""
        count = 0
        for x in system_arr_1:
            temp = x
            if x == i:
                count = 1
                break
        if temp == None:
            print("Made it in here")
            break
        if count == 1:
            continue
        reject.append(temp)
    for y in reject:
        print(y, end="")


def SAME_NAME():
    for i in system_arr_1:
        for x in system_arr_2:
            if x == i:
                together.append(x)
    for y in together:
        print("In both " + y)
