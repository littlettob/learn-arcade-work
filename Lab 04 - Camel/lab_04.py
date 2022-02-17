
#Camel Game Due 2/17/2022
import random

# Introduction to the game
print("""Welcome to Camel!")
You have stolen a camel to make your way across the Mobi Desert.
The natives want their camel back and are chasing you down! Survive your
Desert trek and out run the natives.""")

# create all the variables
oasis = -1
playerdistance = 0
nativedistance = -20
cameltiredness = 0
thirst = 0
canteen = 3

done = False

# make a game loop
while not done :
    # user options to pick
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")



    # user's input choice
    user_choice = input("What will you do? ")

    # if user want to quit
    if user_choice.upper() == "Q" :
        done = True
    # status update for user
    elif user_choice.upper() == "E" :
        print("Miles traveled:", playerdistance)
        print("Drinks in canteen:", canteen)
        print("The natives are", playerdistance - nativedistance, "miles behind you.")

    # if user choice to stop for the night
    elif user_choice.upper() == "D" :
        cameltiredness = 0
        print("Camel is happy")
        nativedistance += random.randrange(7, 14)

    # if user choice to full speed ahead
    elif user_choice.upper() == "C" :
        miles = random.randrange(10, 20)
        playerdistance += miles
        thirst += 1
        cameltiredness += random.randrange(1, 3)
        nativedistance += random.randrange(7, 14)
        # chance of finding an oasis
        oasis = random.randrange(20)
        if oasis == 10 :
            thirst = 0
            cameltiredness = 0
            canteen = 3
            print("You travel upon an oasis!")
            print("your canteen and your stomach filled with water")
        else :
            print("You move forward total of", miles, "miles")
            print("More Thirty")
            print("The natives still chasing.")

    # if user choice to mid-speed ahead
    elif user_choice.upper() == "B" :
        miles = random.randrange(5, 12)
        playerdistance += miles
        thirst += 1
        cameltiredness += 1
        playerdistance += random.randrange(7, 14)

        # chance of finding an oasis
        oasis = random.randrange(20)
        if oasis == 10 :
            thirst = 0
            cameltiredness = 0
            canteen = 3
            print("You travel upon an oasis!")
            print("your canteen and your stomach filled with water")
        else :
            print("You move forward total of", miles, "miles")
            print("More Thirty")
            print("The natives still chasing.")


    # if user choice to drink from canteen

    elif user_choice.upper() == "A" :
        if canteen > 0 :
            canteen -= 1
            thirst = 0
            print("You are thirsty")
        else:
            print("Your canteen is empty.")

    # status updates (thirsty)
    if thirst > 6 :
        print("You died of thirst!")
        print("Game Over.")
        done = True
    elif thirst > 4 :
        print("You are thirsty!")
    # distance traveled win check
    if playerdistance >= 200 :
        print("""The natives are getting close!
You made it across the desert! You won!""")

        done = True
    # camel's tiredness status
    if cameltiredness > 8 :
        print("Your camel is dead.")
        print("The natives catch you and kill you")
        print("Game Over.")
        done = True
    elif cameltiredness > 5 :
        print("Your camel is getting tired.")


    # Natives distance from you
    if playerdistance - nativedistance <= 0 :
        print("The natives have caught up with you!")
        print("Game Over.")
        done = True
    elif playerdistance - nativedistance < 15 :
        print("The natives are getting close!")

#the message from win or lose or quit game
print("Exiting Game.")
input()