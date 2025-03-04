# Authors: Jacob Coleman, Kalid Mohammed
import random

N = 3
points = 20
print("You start off with", points,"points")
while points > 0:
    correct_door = str(random.randint(1, N))
    print("There are " + str(N) + " doors!")
    while points > 0:
        user_input = str(input("Give me your best guess (USE 'h' FOR HINT): "))
        if user_input == 'h':
            hint_door = str(random.randint(1, N))
            while hint_door == correct_door:
                hint_door = str(random.randint(1,N))
            print("it is not the", hint_door, "door")
            points -= 5
        elif user_input == correct_door:
            points += 10
            N += 3
            print("You got the right door! you are now at " + str(points) + " points and there will now be 3 more doors!")
            break
        else:
            print("Wrong door! -10 points!")
            points -= 10

print("you lost at " + str(N) + " doors!")