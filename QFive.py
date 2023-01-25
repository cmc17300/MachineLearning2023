# Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
# Calculate the circumference of a circle and assign the value to a variable name of
# _circum_of_circle_
# Take radius as user input and calculate the area.

import math as m

radius = float(input("Enter radius of given circle: "))
area_of_circle = m.pi * radius * radius
print("Area of the given circle is: %.2f" % area_of_circle)
circum_of_circle = 2 * m.pi * radius
print("Circum of circle is: %.2f" % circum_of_circle)



