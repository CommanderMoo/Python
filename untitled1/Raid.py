from sys import exit


def bank():
    print("If you went to the bank for some money. Which how much would you deposit?")
    
    # user input
    choice = input("> ")

    if "0" in  choice or "1" in choice:
        # user choice
         how_much = int(choice)
        # otherwise
    else:
        dead("Invalid_ INput__")

    how_much = 100

        # GIVE less then 500
    if how_much > 500:
        print("You just saved someones life. Thank you.")
        end()

    elif how_much < 300:
        print("Small deposit for future car insurence. Nice.")
        end()
        # otherwise
    else:
        dead("Invalid_ INput__")


# just because
def end():
    print("Cops bust in the bank and arrest everyone. To find out you were only depositting money.\n Good Work!")
    exit(0)


def theVan():
    print("Does everyone know the plan?\n")
    print("Great! Because theres no turning back now.\n")
    print("We need to be in and out of the bank in less then 30 minutes.")
    print("In other words, I will be gone in 27 minutes.")
    print("Check your gear before you head out\n")
    print("""* 1.Check Utilities *\n* 2.Check Gas Mask *\nOr\n* 3.Check yourself *""")

    # booool
    plan_memorized = False

    while True:
        # user input
        choice = input("> ")

        #  == "Check Utilities" == "check utilities"
        if choice == "1": # (check utilities)
            dead("Your laughing bomb explodes..\nThis makes you and your team laugh all the way down to jail.")
            exit(0)
             
            #  == "Check Gas mask" == "Check Gas Mask" 
       # elif choice == "check gas mask"and not plan_memorized:
           # print("You: Welp things are about to get hairy.")
           # print("Your team gives you the death gaze and repeats the plan again.")
           # continue

            #  == "Check Gas mask" == "Check Gas Mask"
        elif choice == "2": # (Check mask)
            print("You: everyone gear up!")
            bank()

        elif choice == "3": # (check backpack)
            print("Lets move out!!")
            print("That means you put down your game.\nLETS GO!")
            bank()
            
        elif choice == "3": # (Check yourself)
            print("Get in there and count the cameras so we know where we can be seen")
            print("\nTry not to look too suspisious..")
            dead()


def dead(why):
    print(why, "COPS: You have been surrounded!!")
    exit(0)


    # this works

def start():
    print("Either your in or your out man. No pressure.")
    print("You: Im in I just need to get ready first..")
    print("You: Just let me think...")
    print("""* Straight to it *\nOr\n* Prep First *""")

    # user input
    choice = input("> ")

     # == "Straight to It" == "Straight To It"
    if choice == "straight to it":
        bank()

        #  == "Prep first" == "Prep First"
    elif choice == "prep first":
        theVan()

    else:
        dead("Right when we were getting good you just die. wow")


start()



