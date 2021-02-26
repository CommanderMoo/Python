# from <file> import <class>
# <folder><file> import <class>
from oenthree.Enemies import footSoldier, footTank
from oenthree.Mutants import Monsters
from oenthree.TurtleTeam import Metal, CJ


# making turtles
class Turtles:
    def __init__(self, name, health, attackDamage):
        self.attackDamage = attackDamage
        self.name = name
        self.health = health

    def speech(self, stuffToSay):
        print(stuffToSay)

    def eatPizza(self):
        print("Kawabunga Dude")


# # turtle team
# Metal = turtlePower("MetalHead", 200, 5)
# CJ = turtlePower("Casey Jones", 100, 20)


# orange red blue purple
Splinter = Turtles("Splinter", 70, 100)
Mikkie = Turtles("Mikkie", 100, 55)
Ralph = Turtles("Ralph", 100, 85)
Leo = Turtles("Lenard", 100, 65)
Donny = Turtles("Donny", 100, 35)

# footClan units
# footSoldier = footClan("Foot Soldiers", 100, 25)

# monster units
MonsterOne = Monsters(50, 5)


# function one
def player():
    print("---" * 10)
    playerName = input("What is your name creature?")
    print("\n" + Splinter.name + ": This is your home now " + playerName)
    print("\t Meet your new family.")
    print("")
    print(Mikkie.name + ": Hey wassup new dude call me little MICKIEE!!")
    print("")
    print(Ralph.name + ": We're not family, but if you want to fight. I'll be there.")
    print("")
    print(Donny.name + ": Not all of us are crazy and/or angery. Hi, call me Donny.")
    print("")
    print(Splinter.name + ": And last but not least. Wait where is the oldest?")
    print("")
    print(Leo.name + ": I'm here father. Hello " + playerName + ", my name is Leo but we can do introductions later. \n")
    print("---" * 10)
    print("\t Since your new you get to choose what our next move is. \n")
    userChoice = input("*** Either we can talk on the streets of NYC /1/ or talk now /2/ *** ")
    print("---" * 10)
    if userChoice == "1":
        print(Leo.name + ": Sure I guess we have a minute.")
        print("")
        introDuctions()
    elif userChoice == "2":
        print("\t Then we are decided.")
        print("\t Let's move!")
        story()
    return playerName


def story():
    print("---" * 10)
    print(Leo.name + ": Earlier this evening, NYC had gotten some new visitors. \n")
    print(Donny.name + ": I had a friend of ours do a scan of the city while we were covering introductions. ")
    print("\t HEY! " + Metal.name + " show them what you found. \n")

    print(Metal.name + ": H3110 TURT13S, I HAV3 L0CAT3D KRANG 1N TH3 AR3A.")
    print(Donny.name + ": *sigh* My intellect precides me, great job metalhead return home.")
    print(Metal.name + ": AFF1RMATIV3 CR3AT0R. R3TURN1N6 H0M3 \n")

    print(Leo.name + ": It's time to hit the streets. We need to keep the city safe.\n")
    print(CJ.name + ": What exaclty do these \"Krang\" look like exaclty? \n")
    print(Mikkie.name + ": They kinda look like the alien dudes we fought after Dr.Rockwell!")
    print("\t Hey wait! guys I think we might have company. Oh nevermind its just Casey. \n")

    print(Ralph.name + ": Welcome to the party, ready to bust some heads? \n")
    print(CJ.name + ": We both know the answer to that question. *High-Fives Ralph* \n")
    print(Donny.name + ": If we are dealing with the Krang again, we are in big trouble.")
    print("\t Wait do you guys hear that.")
    print("")
    print(Ralph.name + ": Sounds like it's time to knock some heads. \n")
    print(CJ.name + ": Race ya Ralph!! \n")
    storyTwo()


def storyTwo():
    print("---" * 10)
    print(Leo.name + ": Below us, there will be foot soldiers and krang.")
    print("\t There is about 10 " + footSoldier.name + "'s here, but I dont think they came alone.\n")
    print(Ralph.name + ": They're armored ")
    print("\t They have {}".format(footSoldier.health) + " health and " + "{} damage each.".format(footSoldier.damage))
    print("\n" + Leo.name + ": Watch your shells guys.")
    print("\t Wait what is that...?\n")
    print(Mikkie.name + ": Those are some BIG GUNS, on a LOT of " + footTank.name + ".")
    print(CJ.name + ": OK shows over new dude its time for us to get to work!")
    end()


def end():
    print("---" * 10)
    print("Thanks for playing the story will continue soon.")
    exit()


def introDuctions():
    print(Ralph.name + ": Well then, who will go first? \n")
    print(Mikkie.name + ": Back at it again ALRI \n")
    listOfEnemies = ["Foot Clan", "Krang", "Rat King"]
    print(Ralph.name + ": You know what NO!, I will go first.")
    print("\t I am Ralph and I am Rage. ")
    print("\t I hate the " + listOfEnemies[0] + " but I will always enjoy beating ")
    print("\t the shell off the " + listOfEnemies[2] + ".\n ")
    print(Donny.name + ": I will second that motion and also say I am all the brains you'll need.")
    print("\t I fear the only problems we will run into is the " + listOfEnemies[1] + ".")
    print("\t Intelligent yet extremely dangerous. Imagine a human brain with eyes and can talk telegraphically.\n")
    print(Mikkie.name + ": Those guys give me the creeps. They're just so pink and slimy.\n")
    print(Leo.name + ": I guess last again is me. I have one focus and that is protecting my family.")
    print("\t And the main person who I ; who we will stop ; is the Shredder.\n")
    print(Splinter.name + ": Just remember not to underestimate your enemies, especially him.")
    print("\t Now that everyone is acquainted, go be safe my sons.\n")
    print("---" * 10)
    userChoice = input("*** Either we can talk on the rooftops of NYC /1/ or talk later /2/ *** \n")
    print("---" * 10)
    if userChoice == "1" == True:
        print(Leo.name + ": Then we are decided.")
        print("\t Let's move!")
        story()
    elif userChoice == "1" != True:
        print("\t See ya later then.")
        print("\t Turtles, Let's move!")
        exit()
        return


def main():
    player()
    story()
    storyTwo()
    end()


main()