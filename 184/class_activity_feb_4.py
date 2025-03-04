
"""
    In a room of 100 people, 99% are left-handed. How many left-handed people need 
    to leave the room to bring that percentage down to P% (P is an input)
"""

P = eval(input("current percentage = 99%\nNew percentage = "))
P /= 100
left_handed = 99
right_handed = 1
counter = 0
while 1-(right_handed/left_handed) >= P:
    print(1-(right_handed/left_handed))
    left_handed -= 1
    counter += 1
counter -= 1
print("New Value = ", 1-(right_handed/left_handed))
print("Number Of Lefties Left: ", counter)