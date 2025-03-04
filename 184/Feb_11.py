# Class activity for febuary 11th
"""
a = 10
b = 10
print(a==b)
print(a!=b)
print(a is a)
print(a is b)
print(a is not b)

a= 9099
print(id(a))
a+=10
print(id(a))

x = eval(input("Number "))
y = int(x>0) * x
print("ReLU(" + str(x) + ") = "+str(y))

x = eval(input("Number "))
y = ((x<0)* x *(-1) or (x>0) * x)
print(x)

grade = float(input("Enter your grade: "))
if grade >=60:
    print("Congrats you passed!")
else:
    print("Im sorry you failed")
"""

num = eval(input("number "))
if num < 0:
    num *=-1
print(num)