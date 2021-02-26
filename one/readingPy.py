def writeData():
    obj_file = open("RussLanguage.txt", "w")
    obj_file.write("Speak('Hello, this is the program.\n') ")
    obj_file.write("Speak('The book will provide you with everything you need. \n') ")
    obj_file.write("Speak('Everything you are seeing here is being\n ') ")
    obj_file.write("Speak('printed through a if, else, and a for statements.\n') ")
    obj_file.write("Speak('Goodbye from the program.') ")
    obj_file.close()


def readData():
    print("\n\n\n\t ******** Running Russ Programing Language application ******** \n")
    obj_file = open("RussLanguage.txt", "r")
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
    print("\n\n\t ******** End of Russ Programing Language application ******** \n")


def speakToScreen(textToSpeak):
    print(textToSpeak)


writeData()
readData()

