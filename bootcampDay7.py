# *********Lecture - 07 *********

import random




def CheckResults(computer, user):

    if computer == user:

        return 0

    elif computer == 0 and user == 2:

        return -1

    elif computer == 1 and user == 0:

        return -1

    elif computer == 2 and user == 1:

        return -1

    else:

        return 1




def ScoreBoard(score, scoreboard):

    if score == 0:

        print("Its a Draw")

    elif score == -1:

        print("You Lose!")

        scoreboard = scoreboard - 1

    else:

        print("You Win!")

        scoreboard = scoreboard + 1

    print("Your Score Board: ", scoreboard)

    return scoreboard




scoreboard = 0

checker = flag = True

while flag:

    computer = random.randint(0, 2)

    while checker:

        user = int(input("Enter 0 for Stone, 1 for Paper and 2 for Scissors: "))

        if user >= 0 and user < 3:

            checker = False

        else:

            print("You have entered a wrong input... Try Again!!!\n")




    score = CheckResults(computer, user)

    checker = True

    names = ["Stone", "Paper", "Scissors"]

    print("Computer: ", names[computer], " VS User:", names[user])

    scoreboard = ScoreBoard(score, scoreboard)

    if scoreboard >= 2 or scoreboard < 0:

        flag=False

print("\nYour Final Score Board: ", scoreboard)

print("Thanks for playing!!")