import Fighters

# this will be the opening scene


# I can use file input and output to represent a book.
def writeData():
    obj_file = open("Book.txt", "w")
    obj_file.write("Speak('This is the Origin story of Four Legendary Fighters.\n')")

    obj_file.write("Speak('The first fighter is the Tank.')")
    obj_file.write("Speak('\t ...Strong like the Mountains...\n')")
    obj_file.write("Speak('The second fighter is the Healer.')")
    obj_file.write("Speak('\t ...Protector of Many...\n')")
    obj_file.write("Speak('The third fighter is the Scout.')")
    obj_file.write("Speak('\t ...Master of Deception...\n')")
    obj_file.write("Speak('The is the Fighter.')")
    obj_file.write("Speak('\t ...Master of Deception...\n')")
    obj_file.write("Speak('------------------------------------\n')")
    obj_file.write("Speak('The Legend states, that the Four Legends will meet each other.\n')")
    obj_file.write("Speak('That of which is inevitable.')\n")
    obj_file.write("Speak('One of the Legends will try to leave due to inequality.')\n")
    obj_file.write("Speak('Another will be harmed beyond repair.')\n")
    obj_file.write("Speak('The third will return broken.')\n")
    obj_file.write("Speak('But the final will bring the team back together.')\n")
    obj_file.write("Speak('Only together can the Legends attempt to face the coming threat.\n')")
    obj_file.write("Speak('And only the gods can foresee the outcome.')")


def readData():
    print("\n\n\t ******** Origin Story: Begin ******** \n")
    obj_file = open("Book.txt", "r")
    codeLines = obj_file.readlines()
    obj_file.close()
# thanks
    for line in codeLines:
        if line.find("Speak(") != -1:
            proccessed_code = line
            proccessed_code = proccessed_code.replace("Speak('", '')
            proccessed_code = proccessed_code.replace("')", '')
            speakToScreen(proccessed_code)
        else:
            print("\nSyntax error on line: " + line + "\n")
    print("\n\t ******** Origin Story: End ******** \n")


def speakToScreen(textToSpeak):
    print(textToSpeak)


def __main__():
    readData()
    Fighters.story()


__main__()