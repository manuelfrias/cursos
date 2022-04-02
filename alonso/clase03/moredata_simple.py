def main():

    sum = 0.0
    count = 0
    moredata = "yes"

    while True:

        x = float(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)?")
        if(moredata[0] != 'y'):
            break

    print("\nThe average of the numbers is", sum / count)


main()
