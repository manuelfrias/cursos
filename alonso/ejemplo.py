# 1.- Many companies pay time-and-a-half for any hours worked above 40 in a given
# week. Write a program to input the number of hours worked and the hourly rate and
# calculate the total wages for the week

print('mensajito')

hours = eval(input("Please enter the amount of hours "))
rate = eval(input("Please enter the hourly rate "))

totalwages = 0

hoursover40 = 0

totalhours = 0

if hours > 40:
    hoursover40 = hours - 40
    totalhours = 40 + hoursover40 * 1.5
else:
    totalhours = hours

totalwages = totalhours * rate

print("The total wage is " + str(totalwages))
