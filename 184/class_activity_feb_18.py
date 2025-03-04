"""
    This is the class activity for Febuary 18th, 2025
    This is mainly about random
    Generate a random number [1,100] and prints the summation of its digits
"""
import random as r


def random_sum():
    a = eval(input("Enter a number: "))
    print(a, " Is the original number")
    sum = 0
    while a % 10 != a:
        sum += a%10
        a = int(a/10)
    sum += a

    return sum

print(random_sum(), " This is the sum of all digits")

# def random_sum():
#     a = r.randint(1,100)
#     if a == 100:
#         return 1
#     elif a < 10:
#         return a
#     else:
#         return (a%10) + int(a/10)
# print(random_sum())
