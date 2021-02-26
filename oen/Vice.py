# import CIA
from oen.CIA import LA
from oen.CIA import Houston
from oen.CIA import WashingtonDC

# inheritance
# create a class to derive from another


class Scientist:
    def __init__(self, name, age):
        # encapsulation 2
        self.__CIA = "We are actually clones of each other"
        self.name = name
        self.age = age


Krieger = Scientist("Krieger", "40")


class archerVice:
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        # self.power = power
        self.rank = rank


Archer = archerVice("Archer", 37, "Field Specialist")
Pam = archerVice("Pam", 40, "Street Fighter")
Cyril = archerVice("Cyril", 39, "Private Investigator")
Lana = archerVice("Lana", 35, "Weapons Specialist")
Ray = archerVice("Ray", "37", "Cyborg")


class CIA(archerVice):
    def Complain(self):
        return Archer.name.capitalize() + "! "


Slater = CIA("Slater", 42, "Officer")
Malory = CIA("Malory", 70, "Operative")
Holley = CIA("Holley", 55, "Commander")


def instructions():
    print("-----" * 3)
    print("In the following section there will be a story for you to enjoy. ")
    print("In order to view this story please input your name.")
    usrName = input("Please type your name here. \n")
    print("Thanks for typing " + usrName + ".Now please input a number between 1 and 3.")
    usrNum = input("Please type your favorite number here.\n")
    listOfFlips = ["Backflip", "Frontflip", "Barrel Roll"]
    if usrNum == "one":
        listOfFlips[0]
    elif usrNum == "two":
        listOfFlips[1]
    elif usrNum == "three":
        listOfFlips[2]
    else:
        print("invalid")
        exit()
    print("Thanks for inputting your number.")
    print(usrName + ": Since you chose " + usrNum + " you can guess what kind of flips archer will do at the end of "
                                                    "the story.")
    print(listOfFlips)
    print("Now without further delay, enjoy!")
    print("-----" * 3)


def story(objL, objW, objH):

    # print(Ray.name + ": " + str(objL.state))
    print(Malory.Complain())
    print("")
    print(Archer.name + ": WOODHOUSE WHEN YOUR DONE HIDING, MAKE ME A SANDWICH!")
    print("Also, why are there so many ants in here?")
    print("")
    print(Krieger.name + ": Because they are my new and improved zombie ants!")
    print("")
    print(Archer.name + ": Holy *** " + Krieger.name + "!! Thats frickin awesome!!")
    print("")
    print(Malory.name + ": WHO THEY HELL is yelling and why are there so many ants in here?")
    print("")
    print(Krieger.name + ": STOP!!! DONT KILL THAT ANT!")
    print("")
    print(Krieger.name + ": ANNDDD because they are my new and improved zombie ants!")
    print("")
    print(Malory.name + ": And why the hell are you playing with zombie ants?")
    print("\t What are you 2 years old??")
    print("")
    print(Ray.name + ": more like 2000 years old.")
    print("")
    print(Krieger.name + ": Remember who gave you those legs.")
    print("")
    print(Slater.name + ": ANNDDD thanks for confirming why WE are here.")
    print("")
    print(Cyril.name + ": You and Who?")
    print("")
    print(Holley.name + ": And by WE he means me your favorite CIA " + Holley.rank)
    print("")
    print(Holley.name + ": Now can we please get this over with as quick and painless as possible.")
    print("")
    print(Krieger.name + ": *sigh* I never get to have any fun.")
    print("")
    print(Ray.name + ": Says the person who literally has been crafting cyborgs his entire life. ")
    print("")
    print(Pam.name + ": Not to mention our friend Berry is still out there, somewhere.")
    print("")
    print(Archer.name + ": " + Pam.name + ", PLEASE shutup.")
    return objL, objW, objH


def slushAccount(objL, objW, objH):
    print("")
    print(Malory.name + ": First off, that terminator ripoff is stuck in LA! ")
    print("And unless you want to be on the next plane to see him I think you keep your mouths shut!")
    print("")
    print(Ray.name + ": Viva " + str(objL.location))
    print("")
    print(Pam.name + ": OMG I just had an idea. We should totally go see the " + str(objL.teams))
    print("")
    print(Lana.name + ": That didn't really go as you planned huh, Malory?")
    print("")
    print(Malory.name + ": sighhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    print("")
    print(Archer.name + ": Come on now mother, you should've expected that one and also, I call flying the plane.")
    print("Because you know what they say. " + str(objL.state))
    print("")
    print(Lana.name + ": First, No. Second, shut up.")
    print("")
    print(Archer.name + ": I mean..")
    print("")
    print(Slater.name + ": Nope, Nope, Nope. Shut Up like she said.")
    print("All of you failures are going, apologies Malory but that includes you so have fun.")
    print("")
    print(Holley.name + ": We on the other hand need to catch a flight to the" + str(objH.state) + "state.")
    print("")
    return objL, objW, objH


def final(objL, objW, objH):
    print(Malory.name + ": Kriegar, your " + Krieger.age + " act like it.")
    print(Malory.name + ": Ray, stop acting like your " + Ray.age + " and get us a plane.")
    print("")
    print(Ray.name + ": Do you even know when my birthday is?")
    print("")
    print(Malory.name + ": Archer my son would you like to fly the plane to LA with the team....")
    print("")
    print(Ray.name + ": OK IM PACKING, JESUS!")
    print(Malory.name + ": Cyril, Pam, get it together.")
    print(Malory.name + ": Lana, come. Lets drink and look at baby pictures.")
    print(Malory.name + ": And finally my own child. Where is he anyway?")
    print("")
    print("*** Meanwhile over " + str(objW.location) + " ***")
    print(Archer.name + ": I wonder how big" + str(objW.location) + "is but then again, I'll know in a sec!")
    print("Berry: I hate to be jealous of Archer, but he sure does know how to flip....")
    print("")
    print("")
    print("\t*** Thanks for Viewing ***")
    return objL, objW, objH




if __name__ == '__main__':
    objL = LA()
    objH = Houston()
    objW = WashingtonDC()
    instructions()
    objL, objW, objH = story(objL, objW, objH)
    objL, objW, objH = slushAccount(objL, objW, objH)
    objL, objW, objH = final(objL, objW, objH)


# make archer say something and bring everyone in the same room
# bring berry in the picture as soon as u make krieger run away




