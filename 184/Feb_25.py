"""
sum = 0

while True:
    try:
        number = float(input("Enter this "))
        if number == 0.0:
            continue
        if number <0:
            break
        sum += number
    except:
        print("Enter a vaild number!")
print("Sum of the number would be", sum)


user_text = ''
while True:
    line = input("enter your line> ")
    if line.startswith("#"):
        continue
    elif line=='done':
        break
    user_text += line + "\n"

print(user_text)

number = int(input("Enter a positive integer: "))

for j in range(1, number + 1):
    factorial = 1
    for i in range(1, j+1):
        factorial *= i
    print(str(j) + "! = " + str(factorial))
    """
complete = ""
num_stars = 5
backwards = num_stars
for i in range(num_stars):
    i = abs(i - backwards)
    for j in range(i):
        complete += "*"
    complete += "\n"
print(complete)
