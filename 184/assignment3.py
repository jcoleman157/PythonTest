
# Develop a simple calculator that takes in numbers num1 and num2, and one of the four
# operators +, -, /, * and prints the results of num1 operator num2


num1 = eval(input("Please give me number one: "))
operator = input("Please give me an operator one: ")
num2 = eval(input("Please give me number two: "))

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '/':
    print(num1/num2)
else:
    print(num1*num2)


# Develop a guessing number game. First, the user decides the level of the game: easy,
# medium, or difficult. You can design any menu (with print and input functions) that you
# want for this. For each level, the user has 3 guesses. On the third guess (if already not
# won), you will give a hint to the user to either go higher or lower. The game levels are
# distinguished based on the random number range, as Easy: [1, 5], Medium: [1, 20], Hard:
# [1, 50]

import random as r
difficulty = input("Welcome to the guessing game.\nWhat difficulty would you like? ")
rand = 0
if difficulty == 'easy':
    rand = r.randint(1,5)
elif difficulty == 'medium':
    rand = r.randint(1,20)
else:
    rand = r.randint(1,50)
guess = 0
counter = -3
while guess != rand:
    guess = eval(input("What is your guess? "))
    counter += 1
    if counter % 3 == 0 and guess > rand:
        print("Hint: your last guess was bigger than the number!!")
    elif counter % 3 == 0 and guess < rand:
        print("Hint: your last guess was smaller then the number!!")

print('Congrats the number was '+ str(rand))


# A program to prompt for a score between 0 and 100. If the score is out of range, print an
# error message. If the score is between 0 and 100, print a grade using the following table


grade = eval(input("Give me your grade: "))

if grade >=0 and grade <= 100:
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")



# Take a day, month, and year as input and determine if it is a valid date. Consider leap years
# (divisible by 4, but not by 100 unless also divisible by 400). You will print a message
# indicating if the date is correct or not. You should tell user how to insert the date and that
# is your choice to define the input format; you can take day, month, and year separately or
# altogether

month = eval(input("Give me a month (1-12) "))
day = eval(input("Give me a day "))
year = eval(input("Give me a 4 digit year "))
notRealDate = 0
if month >= 1 and month <= 12:
    if day >= 1:
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day <=29:
                    notRealDate = 1
            else:
                if day <= 28:
                    notRealDate = 1
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day <= 31:
                notRealDate = 1
        else:
            if day <= 30:
                notRealDate = 1

if notRealDate == 0:
    print("Not valid date")
else:
    print("Valid date")

# Ask the user to input two numbers: one for the month (1–12) and one for the day. First
# validate that the day is possible for the given month (e.g., February has 28 days, April has
# 30, etc.). Then, determine which season the date falls in. For example, assume:
# ● Winter: December 21 to March 19
# ● Spring: March 20 to June 20
# ● Summer: June 21 to September 21
# ● Fall: September 22 to December 20
# ● Invalid date: for wrong inputs

month = eval(input("Month "))
day = eval(input("Day: "))
if day >= 1:
    if month == 12 and day >= 21:
        print("Winter")
    elif month == 3 and day <= 19:
        print("Winter")
    elif month == 1 or month == 2:
        print("Winter")
    elif month == 3 and day >= 20:
        print("Spring")
    elif month == 4 or month == 5:
        print("Spring")
    elif month == 6 and day <= 20:
        print("Spring")
    elif month == 6 and day >= 21:
        print("Summer")
    elif month == 7 and month == 8:
        print("Summer")
    elif month == 9 and day <= 21:
        print("Summer")
    elif month == 9 and day >= 22:
        print("Fall")
    elif month == 10 and month == 11:
        print("Fall")
    elif month == 12 and day <= 20:
        print("Fall")
