# Import packages
import sys
import random

# false
rolling = True
# neitehr foo or bar is actually called so I'll do so.
# was 12
foo = "Odd"
# was 0
bar = "Even"

while rolling == True:
    query = input("Roll 12 sided Dice, type your numerical guess! (press enter to quit) ")

    machine_prediction = random.randint(1, 8)
# outputs nothing
    # if query == "":
        # sys.exit()
    if query == "":
        print(query)
        # this is for UI, specifically for the user
        sys.exit("C you later snake...")

    if query == machine_prediction:
        print("correct")

    elif machine_prediction == 1:
        print(foo + "1")


    elif machine_prediction == 2:
        print(bar + "2")


    elif machine_prediction == 3:
        print(foo + "3")


    elif machine_prediction == 4:
        print(bar + "4")


    elif machine_prediction == 5:
        print(foo + "5")

    elif machine_prediction == 6:
        print(bar + "6")

    elif machine_prediction == 7:
        print(foo + "7")

    elif machine_prediction == 8:
        print(bar + "8")

    # a duplicate
    # elif machine_prediction == 8:
        # print()

    elif machine_prediction == 9:
        print("Negative")

    # machine preditction ranges from 1-8
    # stated on line 14

    elif machine_prediction == 10:
        print()

    elif machine_prediction == 11:
        print()

    # fixed syntex error
    elif machine_prediction == 12:
        print()