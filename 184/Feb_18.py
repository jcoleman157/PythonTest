# Class Febuary 18th
"""
    This program will take 3 sides of a triangle and figure out if its real
"""
def tri_test():
    a = eval(input("Side number 1: "))
    b = eval(input("Side number 2: "))
    c = eval(input("Side number 3: "))

    if(a+b>c and b+c>a and c+b>a):
        return "This is real"
    else:
        return "Fake ash"
    
# print(tri_test())

"""
    Short circuiting thing
"""
def short_circ():
    x = 6
    y = 0
    print(x>=2 and y != 0 and (x/y) > 2)
    print(x>=2 and (x/y > 2) and y != 0)

# short_circ()

"""
    Try catch trying stuff
"""
def try_catch_test():
    try:
        a = eval(input("Side number 1: "))
        b = eval(input("Side number 2: "))
        c = eval(input("Side number 3: "))

        if(a+b>c and b+c>a and c+b>a):
            return "This is real"
        else:
            return "Fake ash"
    except:
        print("Invalid input. Please enter numeric values for the side lengths.")
        try_catch_test()
try_catch_test()