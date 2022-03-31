
# 3.- Write a program that determines the distance ** in miles **to a lightning strike based on the time elapsed between the flash and the sound of thunder. The speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft.

import math

time = eval(input('Insert the time between the lighting strike and the sound '))

lightning_dist_miles = 1100 * time / 5280

print('The distance in miles between the lightining... ',
      round(lightning_dist_miles, 2))
