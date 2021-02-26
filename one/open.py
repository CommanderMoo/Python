from nltk.chat.util import Chat, reflections

pairs = [
    # todo: figure out conversation paths
    # todo: Ask for names
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"what is your name ?",
        ["My name is Jack, I'm here for you, so Wassup.", ]
    ],
    # todo: feelings
    # good, alright, ok, fair,
    [
        r"good ?",
        ["Yea, I'm glad to hear that :D", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good.\nHow about You ?", ]
    ],
    [
        r"I'm doing ok",
        ["I am glad to hear that :D ", ]
        # "Are you sure you are doing ok? :[",
    ],
    [
        r"I'm doing alright",
        ["Wanna talk about it?", ]
        # "Why not great?",
    ],
    # todo: Special
    [
        r"sorry (.*)",
        ["Its all good, never mind that", ]
        # "Its alright",
    ],
    [
        r"I'm (.*) doing good",
        ["Nice to hear that", ]
        # "Alright :)",
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]
    ],
    # todo: Greeting
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", "Howdy", ]
    ],

    # todo: Work with theses later
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?", ]
    ],

    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Houston, Texas', ]
    ],
    [
        r"how is the weather in (.*) area?",
        ["Weather in %1 is awesome like always", "Never even heard about %1"]
    ],
    [
        r"i work at (.*)?",
        ["%1 is an nice company, I have heard about it.", ]
    ],
    [
        r"i work in the (.*) industry?",
        ["%1 is an amazing industry.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"whats your favorite sport (sports|game) ?",
        ["I'm a very big fan of Football", "I enjoy chess but I dont think you will call that a sport."]
    ],
    [
        r"who is your favorite (moviestar|actor)?",
        ["Hugh Jackman", "Ryan Reynolds", ]
    ],
    [
        r"goodbye",
        ["HEY! Be careful out there. ;) ", "It was nice talking to you. Hope to see you again soon. :)"]
    ],
]


def main():
    # default message at the start
    print(
        "Hey, I'm Russ 3000 - and I'm here when you wanna talk. Always.")
    print(
        "\nAsk me something, no rush..")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    main()
