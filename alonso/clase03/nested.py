def main():

    print("Select the correct answer.\n")

    # for qnumber in [1,2,3,4,5...20]:
    for qnumber in range(1, 21):

        print("Question", qnumber)

        for qletter in ["a", "b", "c", "d", "e"]:
            print(qletter, qnumber)

        print()


main()
