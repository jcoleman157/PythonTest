# Print average of numbers 1 to 200 that are not divisible by 5
counter = 200
sum = 0
numOfNums = 0
while True:
    counter = counter - 1
    if counter == 0:
        break
    elif counter % 5 == 0:
        continue
    else:
        numOfNums += 1
        sum += counter
adv = sum/numOfNums
print(adv)