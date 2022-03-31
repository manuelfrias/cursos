# 2.- Write a program that calculates the cost per square inch of a circular pizza, given its diameter and price.
# The formula for area is A = pi * r2

import math

price = eval(input('Please enter the price of the pizza '))
diameter = eval(input('Please enter the diameter of the pizza '))

area = math.pi * (diameter/2)**2

# sq inches >> area
# esto te piden >>  $ / sq inch

# print(area) << a veces es bueno imprimir las variables para entender lo que esta pasando

cost = price/area
print('The cost per sqinch is ', round(cost, 2), '\n\n')
