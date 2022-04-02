def main():

    sum = 0.0
    count = 0

    while count < 50:
        x = float(input("Enter a number >> "))
        sum = sum + x
        count = count + 1

    print("\nThe average of the numbers is", sum / count)


main()
