# 1.- The Fibonacci sequence starts 1, 1, 2, 3, 5, 8… Each number in the sequence (after the first two) is the sum of the previous two.
# Write a program that computes and outputs the nth Fibonacci number, where n is a value entered by the user.

n_number = eval(input("Please enter the nth number in the Fibonacci sequence"))

if n_number < 0:
    print('The number cannot be smaller than 1')

elif n_number <= 2:
    print('The Fibonacci number is ', 1)

else:
    antepenul = 1
    penul = 1
    a = 3

    while a <= n_number:
        respuesta = antepenul + penul
        antepenul = penul
        penul = respuesta
        a = a + 1

    print(respuesta)
