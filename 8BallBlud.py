#Anthony Garcia
#1/22/24
#Magic 8 Ball
#initialize
import random
mylist = ["Definitely", "Most likely", "Outlook good", "Ask Again Later", "Better not tell you now", "My sources say no", "My reply is no", "Yikes IDK"]

#functions
def question():
    while True:
        global mylist
        goat = input("What would you like to know?")
        if goat.endswith("?"):
            print (random.choice(mylist))
        else:
            print("Not a question sorry")
        option= input("Would you like to know your fortune? y/n")
        if option == "n":
            break
#main
             

question()