# Russell Pickney Jr
# June 25, 2020// July 1, 2020
# http://media.textadventures.co.uk/games/WcXYblcKtkSx6lJKY_pz7w/index.html
# otp with PH 6/29 1700


# end game
# function five
def end():
    print("******************************")
    print("\nHey thanks for playing")
    userReset = input("Would you like to play again? (y/n)\n")

    # reset code
    if userReset == "y" or "Y":
        print("Run it")
        main()
    else:
        print("play again sometime soon.")


# function four
# called inside of the notebook
def tasks():
    # tasklist array
    tasklist = ["Head Downtown", "Review Notes", "Question Suspects"]

    # create three options for the user to choose from
    userChoice = input("What should I do? 1/2/3 \n")

    # have user type string choice
    if userChoice == "1":
        print("Lets head downtown and see what turns up")
        # a story
        story_choiceOne()
    elif userChoice == "2":
        print("Stop, sit down, and think.")
        # again
        story_choiceTwo()
    elif userChoice == "3":
        print("Its time to hit the streets,\n lets just hope they dont hit back.")
        # again
        story_choiceThree()
    else:
        print("Input error, not a choice")
        tasks()
        # story_choiceFour()
    # here im trying to use the options [0,1,2] to make choices


# title & background
# function three
def detective_land():
    print("Welcome to Detectiveland!")
    print("Respond to the questions with the () answers\n")


# function two
def notebook():
    print("Well lets see what we have today..\n")
    # print("Head Downtown", "Review Notes", "Question Suspects")
    # this ^ is here for better understanding
    print("Either I can take a stroll into the city... \"1\"")
    print("Check my notes again just in case... \"2\"")
    print("Head out to find and question some suspects... \"3\"")
    tasks()


# to be continued
def story_choiceOne():
    print("Well lets get a move on before the sun goes down.")


# to be continued
def story_choiceTwo():
    print("something")


# to be continued
def story_choiceThree():
    print("")


# to be continued
def story_choiceFour():
    print("dang, the police chief is here")
    print("now I will never get to leave")
    end()


# todo: Get the user name
# function one
def story_pieceOne():
    print("Another long working day for Detective... ")
    user_name = input("Hey! Wait is your name again? :")
    print("""
    I'm new to the town but I can read it like a book.
    This isn't exaclty the nice side of town but then again this 
    is better then being there. Here your with real people, and 
    I mean that literally. But now isn't the time to discuss that, 
    lets get to work..:New Texas, 02:34
    """)
    input("Press enter to continue..")
    if input == "enter" or "Enter":
        print("\n" + user_name + ": I've got much to do today, I just don't know where to start.")
    else:
        return user_name


# changed from open "x" because we dont new to create a
# new file
obj_locations = open('Locations.txt', "w")
obj_locations.write("And again!!\n")
obj_locations.write("Have fun, Thanks for Playing\n\n")
obj_locations.close()


# the actual main function
# function zero
def main():
    detective_land()
    obj_locations = open('Locations.txt', "r")
    print(obj_locations.read())
    story_pieceOne()
    notebook()
    end()


# why does this work as the function starter
if __name__ == "__main__":
    main()

"""
use an array to act as a inventory system, 
use add code to 
check if items can go in inventory 
check if item is on field/ rather then in inventory/ or hand 
"""
