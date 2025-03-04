# This is what I will be uploading to github just to show cole what python is all about
# when a line has (#) in it then the rest of the line is commented out

print("Hello World!") # This just prints in the terminal "Hello world"

a = 1 # in some programming langs you might need to specify "int" for integer before the variable, python is not like this
b = 2 # in python there are floats (0.5, 12.323, ect), ints (1,2,3,4), booleans (true/false), Strings (List of characters, sentences)

print(a+b, a-b, a*b, a/b) # These are the 4 "Basic" operators

# When trying to print strings (in either '' or "") and a variable that is not string you have to use a , or change the
# Value of the variable where you are attempting to use it

# Example of this is typing str(var) when using it in a print like seen before or just using the comma version
print("Value of a is + "+ str(a) + "Value of b is = " + str(b))
print("Value of a is +", a , "Value of b is =", b)

# Both of these have the same exact output


# the == in this is a check that returns true or false
if a == b:
    # This is false and will not be entered, so it skips the if and goes to the else of elif (else if)
    print("This is not true")
else:
    print("This will printed")

if a + b == 3:
    print("Hip Hip Horray!")
elif not a+b == 4:
    print("Even though a + b is not 4, this will be skipped due to the fact that if was true")
if not a+b == 4:
    print("Now this will be printed")

# This is a loop
for i in range(1,5):
    print(i) # will print 1,2,3,4 all on sepereate lines

sum = 0
# prints 1, 3, 6, 10, 15 all on different lines
for x in range(1,6):
    x += sum
    print(x)
    sum = x

# This is a method that I can call at any point
def new_method():
    a = 2
    for i in range(1,11):
        print(i*a)

# Will print i * a 10 times
new_method()

# So num will be a paramater (or argument) 
def newer_method(num):
    # will print 1 to num
    for i in range(1, num + 1):
        print(i)
    print("not in the for loop anymore")

newer_method(5) # 1,2,3,4,5
newer_method(10) # 1,2,3,4,5,6,7,8,9,10
