# Hello World program in Python
# make at title    
print("Hello World!\n")

# one
# make an array's / list 
plans = ["Wake Up", "Play Music", "Work", "Sleep"]
print("This is the plan ", plans)

# my favorite part (story strings)
a = """
This is the law of the land:\n 
If you are over 20, you must cook!
If you are under 18, you must clean!!
\n"""
print(a)

print("The way this is going to work is")

b = "I am going to ask a series of questions requiring numbers.\nQuestions like your age height and weight."
print(b)

print("Who ever has the lowest amount of points will get to choose the song.\n")

# tuple time
print("First we will choose the music genre...\nWe have Rap, Country, and Soul music")
music_Types = ("Rap","Country","Soul")
print(music_Types[-3], "has been selected.\n")

# ask the user to answer
user = input('Whats your name first off?\n')

# print("How old are you?", end='')
# age = input()
age = input("How old are you?\t")
height = input("How tall are you?\t")
weight = input("How much do you weigh?\t")
you = (age, 'years old', height,'ft tall and ', weight,'lbs')

print(user, ": I am ", you, ".\n")
print("What song would you like to listen too?\n")

# third
# This are actual songs 
# dictionary
music = {
    "Rich the Kid": "Sick",
    "Anime": "Spice Girl",
    "Kendrick Lamar": "Fear", 
    }

print(music)
song = input("\nSick, Spice Girl, or Fear?")
print("Thanks for playing, TO BE CONTINUED.........")




