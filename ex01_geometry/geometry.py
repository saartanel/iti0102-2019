"""Ask user a shape and a radius or a side length and calculate the shape area."""
import math

shape = input("Please insert geometric shape:")

if shape == "circle":
    radius = float(input("Please insert radius in cm:"))
    area = math.pi * math.pow(radius, 2)
    print("The area is " + str(round(area, 2)) + " cm^2")

elif shape == "square":
    side = float(input("Please insert side length in cm:"))
    area = pow(side, 2)
    print("The area is " + str(round(area, 2)) + " cm^2")

elif shape == "triangle":
    side = float(input("Please insert side length in cm:"))
    area = (math.sqrt(3) / 4) * math.pow(side, 2)
    print("The area is " + str(round(area, 2)) + " cm^2")

else:
    print("Shape is not supported.")
