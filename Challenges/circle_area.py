# Receives the user input for the circle radius
# and calculates the circle area

from math import pi

def circle_area():
    radius = float(input("Enter the circle radius: "))
    area = pi * (radius ** 2)
    return print(f"The area of the circle is: {area}")
    
circle_area()
