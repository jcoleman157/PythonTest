# print(type('2.7'))
# print(1,000,000)

# fisrt 3 did not work

'''
expr1= (1+1)**(5-2)
expr2 = (2**1+1)
expr3 = 2*3-1
expr4 = 2*5/4
expr5 = 5-3-1
'''

# print(str(expr1) + "\n" + str(expr2) + "\n" + str(expr3) + "\n" + str(expr4) + "\n" + str(expr5) + "\n")

def valOfX(y,a,b):
    y = y-b
    x = y/a
    print(x)
    # this might be the hardest class I have ever taken in my life 😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱😱

valOfX(5,2,3)

'''

this is the code I wrote in between writing the stuff above
only condition is the string has to be under 28 in length
I got lazy and didnt want to keep that part dynamic

'''
def nameInBox():
    print('what is your name? ')
    name = input()
    topBot = '------------------------------' # 30
    mid = '|                            |'
    length = len(name)
    space = 28

    # Number of spaces between sides of box with thing
    numOfSpace = int((28/2) - length/2 - 1)

    # creating the name and part of box
    spaceAndName =  '|' + " " * numOfSpace + name +"😻"+ " " * numOfSpace

    # If needed adds an extra space
    if len(spaceAndName) % 2 == 0:
        spaceAndName = spaceAndName + "|"
    else:
        spaceAndName = spaceAndName + " |"


    # printing the final product
    print(topBot+ "\n" + mid + "\n" + spaceAndName + "\n"+mid + "\n"+topBot)


nameInBox()