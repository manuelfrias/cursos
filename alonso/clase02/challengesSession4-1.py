# Write a program to calculate the volume and surface area of a sphere from its
# radius, given its input. Here are some formulas that might be useful:
# V = 4/3* pi *r3
# A = 4*pi*r2

import math

radius = eval(input('Insert the radius '))

volume = 4/3 * math.pi * radius**3
area = 4 * math.pi * radius**2

print('\n\n', 'The volume of sphere is ', round(volume, 2),
      ' The area of sphere is ', round(area, 2), '\n')

# print('The area of sphere is', area)
