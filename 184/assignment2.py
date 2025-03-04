# Author: Jacob Coleman
# This is assignment 2

import math as m


# This program converts kilos to miles
def kilo_to_miles():
    kilos = eval(input("How many Kilos: "))
    miles = kilos * .62
    return miles
# print(kilo_to_miles())


"""
This progrtam:
A program that converts a temperature given in Celsius to Fahrenheit. The formula is:
F = (C * 9/5) + 32
"""

def celsius_to_fahrenheit():
    C = eval(input("How much Celcius "))
    F = (C * 9/5) + 32
    return F

# print(celsius_to_fahrenheit())

"""
This program:
A program to calculate the volume and surface area of a sphere from its radius, given as
input. Here are some formulas that might be useful
V= 4/3πr^3
A= 4πr^2
"""
def vol_and_surface_area():
    r = eval(input("What is the radius "))
    V= (4/3)*m.pi*(r**3)
    A= 4*m.pi*(r**2)
    return V, A

# print(vol_and_surface_area())

"""
This program:
A program that accepts two points and determines the distance between them.
"""
def distance():
    x1 = eval(input("x1 = "))
    y1 = eval(input("y1 = "))
    x2 = eval(input("x2 = "))
    y2 = eval(input("y2 = "))

    distance = m.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return distance

# print(distance())

"""
This program:
A program that solves a quadratic equation of the form ax² + bx + c = 0. The solutions are
given by the quadratic formula:
x = -b +- sqrt(b**2 -(4*a*c))/2a
a, b, c are the inputs. You do not need to handle negative square roots.
"""
def quadratic():
    a = eval(input("a = "))
    b = eval(input("b = "))
    c = eval(input("c = "))

    x1 = ((-1*b) + m.sqrt(b**2 -(4*a*c)))/(2*a)
    x2 = ((-1*b) - m.sqrt(b**2 -(4*a*c)))/(2*a)

    return x1, x2

print(quadratic())

