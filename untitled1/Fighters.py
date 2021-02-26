

class Tank:
    def __init__(self, name, strength, rank):
        self.name = name
        self.strength = strength
        self.rank = rank

    def rank(self):
            print("Tank Class")


class Healer(Tank):
    def rank(self):
        print("Healer Class")


class Fighter(Tank):
    def rank(self):
        print("Fighter Class")


class Scout(Healer):
    def rank(self):
        print("Scout Class")


Russ = Scout("Russ", "Void", "Creator")
Maestro = Tank("Maestro", "Strong ASF", "Teacher")
Mother = Healer("Mother", "No-Scale", "Hell Bringer")
Rivals = Scout("Rivals", "Moderate", "Common")
Father = Fighter("Father", "Strong ASF", "Swivel Speed")
# list done
ListOfFruits = ["Peaches", "Pomegranate", "Strawberry"]
ListOfWeapons = {"Sword":1, "Shield":2, "Bow":3}


def story():
    print()
    print("*** This is how the Story begins. ***")
    print()
    print(Father.name + ": Boy!")
    print(Father.name + ": State your presence and make yourself known.")
    # input clarity is a thing
    usrName = str(input("\n*** WHAT SHALL YOU BE CALLED ***\n"))
    print()
    # this is user input
    print("I am " + usrName + ": son of " + Father.rank)
    # -------------------------------------------------------------------
    print(Father.name + ": AND! Do you DARE DISRESPECT YOUR MOTHER!?!")
    print("I am " + usrName + ": son of " + Father.rank + " and the " + Mother.rank)
    print()
    print(Mother.name + ": I haven't been called that name in ages, it warms me.")
    print(Mother.name + ": Enough pestering the child. " + usrName + "! Let us eat.")
    print(Mother.name + ": Today we will have a combination of " + ListOfFruits[1] + " and " + ListOfFruits[0] + ".")
    print()
    print("*** BANG BANG ON THE DOOR ***")
    print()
    print(Mother.name + ": I wonder who that could be..")
    print(Father.name + ": Make your choice boy.")
    print()
    # -------------------------------------------------------------------
    usrChoice = int(input("*** GET THE DOOR (1) / STAY IN YOUR PLACE (2) ***\n"))
    if usrChoice == 1:
        print(Rivals.name + ": Why hello there.")
        pass
    elif usrChoice == 2:
        print(Father.name + ": Lets find out.")
        print(Rivals.name + ": Why hello there.")
        pass
    else:
        print(usrName + ": They will go away eventually")
        print("*** BANG BANG ON THE DOOR ***")
        pass

    print(Rivals.name + ": I am here looking for the " + Mother.rank)
    print(Father.name + ": On whoms request? ")
    print(Rivals.rank + ": Mine.")
    print()
    print("*** Your father has just been shot by an arrow ***")
    print()
    print(Rivals.rank + ": Come with us.")
    print()
    print("*** Your mother has just grabbed two knives ***")
    print()
    print(Rivals.rank + ": Now.")
    print()
    print("*** Sword (1) / Shield (2) / Bow (3) ***")
    print()
    # -------------------------------------------------------------------
    usrWeapons = int(input("*** What weapon do you choose ***"))
    if usrWeapons == 1:
        print("*** You equipped the Sword and Stood your Ground ***")
        print(usrName + ": Die!")
        print(Mother.name + ": *** Lowers your blade ***")
        print(Mother.name + ": Take care of your father.")
        print(Mother.rank + ": I shall return.")
        print(Rivals.rank + ": *** Knocks you unconscious  ***")
        pass
    elif usrWeapons == 2:
        print("*** You equipped the Shield and Jump to your Father ***")
        print(usrName + ": FATHER!!")
        print(Rivals.name + ": *** Grabs you out of the air ***")
        print(Rivals.rank + ": *** Knocks you unconscious  ***")
        pass
    elif usrWeapons == 3:
        print("*** You equipped the Bow and Sent an Arrow at the Common ***")
        print(usrName + ": I am the son of the " + Father.rank + " and the " + Mother.rank)
        print("*** Common turns his face missing the arrow ***")
        print(Rivals.rank + ": It seems you have missed young one.")
        print(Rivals.rank + ": *** Knocks you unconscious  ***")
        pass
    else:
        print("*** You were shot because you were too slow ***")
        print("*** Your Mother gets hailed away and killed for her rank ***")
        exit()

    print(Rivals.rank + ": No matter what you do boy. You will never win.")
    print(Rivals.rank + ": It is not your time. Now rest child.")
    print()
    print()
    print("*** Wake up outside your house ***")
    print(usrName + ": Wha where am I.")
    print(usrName + ": MOTHER AND FATHER!")
    print("*** Turn around and view flames consuming the fields ***")
    print(usrName + ": I am " + usrName + " son of " + Father.rank + " and " + Mother.rank)
    print()
    print("*** To be continued ***")
    print(Russ.name + ": Thanks for playing")
    exit()