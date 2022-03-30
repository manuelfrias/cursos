# A certain CS professor gives five-point quizzes that are graded on the scale 5-A, 4-
# B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an input and uses a
# decision structure to calculate the corresponding grade.
grade = ''
score = int(input('Please enter the score '))

if (score <= 5) and (score >= 0):
    if score == 5:
        grade = 'A'
    elif score == 4:
        grade = 'B'
    elif score == 3:
        grade = 'C'
    elif score == 2:
        grade = 'D'
    else:
        grade = 'F'
    print(grade)

else:
    print("Try again")
