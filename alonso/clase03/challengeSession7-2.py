# 2.- Write a program that uses a while loop to determine how long it takes for an investment to double at a given interest rate.
# The input will be an annualised interest rate, and the output is the number of years it takes an investment to double.
# Note: The amount of the initial investment does not matter; you can use $1

# 20
rate = eval(input('Please enter the interest rate in years'))

investment = eval(input('Please enter the investment rate'))

time = 0

objective = investment * 2


while True:
    if investment * (1 + (rate / 100))**time > objective:
        break
    
    time = time + 1

print('The time it took to double is ', time, " years")



