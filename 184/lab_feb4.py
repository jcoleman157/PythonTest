import math

def inch_to_cent():
    inches = eval(input("pick number for inches= "))
    return inches*2.54

print(inch_to_cent())

def rect_area_parimiter(length, width):
    length = eval(input("pick number for length= "))
    width = eval(input("pick number for width= "))
    a= length*width
    p= length*2 + width*2
    return a,p

print(rect_area_parimiter(4, 4))

def area_of_triangle():
    a = eval(input("pick number for side 1 = "))
    b = eval(input("pick number for side 2 = "))
    c = eval(input("pick number for side 3 = "))
    s = (a+b+c)/2
    a = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return a

print(area_of_triangle())

def num_of_digits():
    num = eval(input("pick number for number= "))
    return math.ceil(math.log10(num))

print(num_of_digits())