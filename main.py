import sys
import random
import time

def bwaExit():
    
    bwa = input("\ntype 'r' to restart and 'x' to exit. ")
    if bwa == "r":
        print("Restarting...")
    elif bwa == "x":
        print("Exiting...")
        sys.exit()

#################

try:
    def potato_checker():
        while True:
            print("======= Welcome to the Potato Checker! =======")
            print("As we all know, everything in the universe is either a potato, or not a potato, but, the question is.\n" \
            "How do we know what is and what isn't a potato? Well, that's where this tool that I've build comes in! \n" \
            "All you have to do is enter your object, and this magical program will tell you whether it is a potato or not!")
            potato = input("What is your object?: ")
            print("Thinking....")
            time.sleep(random.randint(0,6))
            print("Analysing. Do not interrupt. The universe is fragile.")
            time.sleep(random.randint(0,6))
            print("Consulting the laws of physics, biology, and vibes...")
            time.sleep(random.randint(0,6))
            if potato.lower() == "potato":
                print("That is a potato!")
                bwaExit()
            elif potato.lower() == "fries":
                print("That is not a potato, however, it used to be!")
                bwaExit()
            else:
                print("That is not a potato.")
                bwaExit()
    potato_checker()



except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()