# get the diameter of a circle from the user
diameter = float(input("Enter the diameter of the circle: "))

# calculate the radius
radius = diameter / 2

# calculate the area of the circle
PI = 3.14159
area = PI * (radius ** 2)

print("The area of the circle with diameter " + str(diameter) + " is: " + str(area))