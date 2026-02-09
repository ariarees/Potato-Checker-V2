import sys

def potato_checker():
    while True:
        print("======= Welcome to the Potato Checker! =======")
        print("As we all know, everything in the universe is either a potato, or not a potato, but, the question is. \n " \
        "how do we know what is and what isn't a potato? Well, that's where this tool that I've build comes in! \n" \
        "All you have to do is enter your object, and this magical program will tell you whether it is a potato or not!")
        potato = input("What is your object?: ")
        if potato.lower() == "potato":
            print("That is a potato!")
        elif potato.lower() == "fries":
            print("That is not a potato, however, it used to be!")
        else:
            print("That is not a potato.")
        print("")

def __main__():
    



# except KeyboardInterrupt:
#     print("\nExiting...")
#     sys.exit()

