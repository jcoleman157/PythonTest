

# a = eval(input("Enter a number: "))
# print(a, " Is the original number")
# sum = 0
# while a % 10 != a:
#     sum += a%10
#     a = int(a/10)
# sum += a



# print(sum, " This is the sum of all digits")

"""
Print the average of even numbers from 1 to 100 ([1,100])
"""
# average = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         average += i
# average //= 50
# print("Average for all evens 1-100 is:",average)


for i in range(1, 16):
    if i % 4 == 0:
        print("/\\", end="")
    else:
        print("_", end="")
print("o")