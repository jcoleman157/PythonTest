# num = eval(input("Enter a number: "))
# numbers_sum = 0
# numbers_count = 0

# while num>=0:
#     numbers_count += 1
#     numbers_sum += num
#     num = eval(input("Enter a number: "))

import random as r

# counter = 1
# min = 99999
# max = 0
# while counter <= 10:
#     rand = r.randint(1, 1000)
#     print(rand)
#     if rand < min:
#         min =rand
#     if rand > max:
#         max = rand
#     counter += 1

# print("Largest = ", max,"\nSmallest = ", min)

# my_string = 'Python Programming'
# for c in my_string:
#     print(c)

worm = ""
for i in range(1, 16):
    if i % 4 == 0:
        print("/\\", end="")
    else:
        print("_", end="")
print("o")