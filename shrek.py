import time
import sys
from random import randint

dice_roll = randint(1, 6)

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


class Player:
    """ This is a class that represents the main character in a game. """

    def __init__(self, name):
        self.name = name

    def printname(self):
        print('Welcome', self.name)


p1 = Player('Shrek')

p1.printname()


class Game:

    def start():
        print("\nYou are standing in a large, open field.")
        print("There is a pathway into the woods to your left. To your right, there is a path to the swamp. (l or r)")

        answer = input(">").lower()

        if answer == "l":
            Forest.forest_room()
        elif answer == "r":
            Swamp.swamp_room()
        else:
            Game.game_over("Type l or r next time.")

    def play_again():
        print("\nDo you want to play again? (y or n)")

        # convert the player's input to lower_case
        answer = input(">").lower()

        if "y" in answer:
            # if player typed "yes" or "y" start the game from the beginning
            Game.start()
        else:
            # if user types anything besides "yes" or "y", exit() the program
            exit()

    def game_over(reason):
        print("\n" + reason)
        print("Game Over!")
        Game.play_again()

    # start the game


class Forest:
    def forest_room():
        """
        function that takes player into forest
        meets Fiona
        returns prompt to eithr go to the next room or you lose the game
        """
        print("\nLook! Over there!")
        print("It's a beautiful princess.")
        print("Her name is Fiona.")
        print("Do you want to say hello?(1) Or throw mud at her?(2)")
        print("Type (1) or (2).")
        answer = input("> ")

        if answer == "1":
            print(
                "Fiona asks you a very important question, 'What's my favorite color?' ")
            print(
                "She says if you're incorrect, you are not her true love. Hint: Shrek...")
            answer = input("> ")
            if answer == "green" or "brown":
                print(
                    "\n'That's right!' she exclaims. Now that Fiona is sure of her love, you must go with her to the castle to meet her parents.")
                Castle.castle_start()
            else:
                print(
                    "Nahhhh. Fiona says, 'Byeeeee' and marries your nemesis, Lord Farquaad")
        elif answer == "2":
            Game.game_over("Fiona says, 'Byeeeee' and marries Lord Farquaad")
        else:
            Game.game_over("Better luck next time. Type a number.")


class Swamp:
    count = 0
    questions = {
        "Why can't a nose be twelve inches long?": ["it would be a foot", "then it would be a foot", "foot"],
    }
    question1 = {
        "What is broken when it's not held?": ["A Promise", "Promise", "promises", "your word"]
    }

    def riddle2():
        question2 = {
            "I can run, but not walk. Thought is not far behind me. What am I?": ["Nose", "a nose"]
        }
        for question, correct_answers in question2.items():
            user_answer = input(f"{question}: ")
            if any(user_answer.lower() == answer.lower() for answer in correct_answers):
                print("Correct!")
            elif(Swamp.count < 2):
                print('Donkey says: "Shrek! That isn\'t an option"')
                Swamp.count += 1
                Swamp.riddle2()
            else:
                Game.game_over('You stink, Ogre')

    def riddle1():
        question1 = {
            "What can't you see, but it's always in front of you?": ["Future", "the future", "your future", "time ahead", "future time"]
        }
        for question1, correct_answers in question1.items():
            user_answer = input(f"{question1}: ")
            if any(user_answer.lower() == answer.lower() for answer in correct_answers):
                typingInput(
                    "You have solved my riddles Ogre, you may continue on your journey to the castle. // Press any button to continue.")
            elif(Swamp.count < 2):
                print('Donkey says: "Shrek! That isn\'t an option"')
                Swamp.count += 1
                Swamp.riddle1()
            else:
                Game.game_over('You stink, Ogre')

    def riddle3():
        question3 = {
            "What can be measured but has not height, width or depth": ["Temperature", " the temperature"]
        }
        for question3, correct_answers in question3.items():
            user_answer = input(f"{question3}: ")
            if any(user_answer.lower() == answer.lower() for answer in correct_answers):
                typingInput(
                    "You have solved my riddles Ogre, you may continue on your journey to the castle. // Press any button to continue.")
            elif(Swamp.count < 2):
                print('Donkey says: "Shrek! That isn\'t an option"')
                Swamp.riddle3()
                Swamp.count += 1
            else:
                Game.game_over('You suck')

    def riddle():
        for question, correct_answers in Swamp.questions.items():
            user_answer = typingInput(f"{question}: ")
            if any(user_answer.lower() == answer.lower() for answer in correct_answers):
                print()
                Swamp.riddle2()
                typingInput(
                    "You have solved my riddles Ogre, you may continue on your journey to the castle. // Press any button to continue.")
            elif(Swamp.count < 2):
                print('Donkey says: "Shrek! That isn\'t an option"')
                Swamp.count += 1
                print(Swamp.count)
                Swamp.riddle()
            else:
                Game.game_over('You stink, Ogre')

    def swamp_room():
        typingPrint('welcome to the swamp')
        typingPrint('n\This swamp is filled with mysterious characters')
        print()
        typingInput('Press any button to continue')

        print("""
                            WWWWWWWWWWWWWW
                    :::::WWWWWWWWWWWWWWWWWWWWWWW
                :::::::::::WWWWWWWWWWWWWWWWWWWWWWW
        /WWWWWWWWWWWWW:::::::::::WWWWWWWWWWWWWWWWWWW    >>>>>>>>>
        WWCCWWWWWWWWWWWWW:::::::::WWWWWWWWWWWWWW >>>>>>>>>>>>>>
            CCCCCCCWWWWWWWWWW:::::::::WWWWWWWWW/>>>>>     >>>>>>>>>
        CCCCCCCCCCCCWWWWWWWWW:::::::::>>WWWWW  >>>>>>>>    >>>>>
        CCCCCCCCCCCCCCCCCWWWWWWWW::::::::>WWWWWW>>>>>>>   >>>>
        CCCCCCCCCCCC            CCCWW:::::::::::>>>>>>>>>>
    CCCCCCCCC          /\       CCCW::::::WWWWWWWWWWWWWW
    CCCCCC \         /`  `\      CCCCW:::::WWWWWWWWWWWWW
        CCCC                          CCCCC::::WWWWWWWWWWW
        CC |~~|                      CCCCCCCCCCCWWWWWW
            | |~||    |~~~~|            CCCCCCCCCCCCCCCC
            |_|*||    |~~| ~|          CCCCCCCCCCCCCCCCCCC
            |_||    |* |  |            CCCCCCCCCCCCCCCC
            |  |    |__| _|                \ CCCCCCCC
        |~~~~~~~~~\   |   |              ~~~|  CCCCCCC
        `\  @      `\ ~~~~  ooo          ^ /` CCCCCC
        /\________/      oooooo         ` CCCCCC
        |                  oooo            |
        `\     ____                       /`
        `\   |**|___                  /`
            `\ ~~|___|                /`
            `\         /    ______/` MMM
                `\__\__/`____/    |   MMMM
                    MMM|   /::::|MMMMMMM
                    MMMM oooo::::MMMMMMMM
                :::::MMMMoooooMMMMMMMMMMMM:::::
                :::::MMMMoooooooMMMMMMMMMM:::::::
            :::::MMMMMooooooMMMMMMMMMM:::::::::
            :::::MMMMMM::oooMMMMMMMMMM::::::::::::
            ::::::MMMMM:::::::MMMMMMMMM:::::::::::::
                MMMM         MMMMMMMM
                    W            MMMMMM
                                WWW """)
        print('Pinocchio appears')
        typingPrint('Ogre, you must solve my ridlles to move on')
        input('press any button to continue')

        while Swamp.count < 3:
            Swamp.riddle()

            Game.game_over(
                "you are not smart enough to reach the castle, Ogre")

    #     elif answer == 'r':
    #         print( """ ,_  .--.
    #              , ,   _)\/    ;--.
    #      . ' .    \_\-'   |  .'    \
    #     -= * =-   (.-,   /  /       |
    #      ' .\     ).  ))/ .'   _/\ /
    #          \_   \_  /( /     \ /(
    #          /_\ .--'   `-.    //  \
    #          ||\/        , '._//    |
    #          ||/ /`(_ (_,;`-._/     /
    #          \_.'   )   /`\       .'
    #               .' .  |  ;.   /`
    #              /      |\(  `.(
    #             |   |/  | `    `
    #             |   |  /
    #             |   |.'
    #          __/'  /
    #      _ .'  _.-`
    #   _.` `.-;`/
    #  /_.-'` / /
    #        | /
    # jgs   ( /
    #      /_/
    #      """)

    #         print('Fairies')
    #         print()
    #         riddle1()
    #     else:
    #         print('Donkey says: "Shrek! That isn\'t an option"')


class Castle:
    def castle_start():

        print("\nYou slowly approach the bridge to Lord Farquads castle...")
        print("\nYou notice 2 points of entry into the castle.")
        print("\nWhich path do you choose?")
        typingPrint("\n1). Enter through the front gates.")
        typingPrint("\n2). Climb the vines on the side of the castle.")

        answer = input(" >")

        if answer == "1":
            Game.game_over("Lord Farquad captured you.  Feels bad man.")
        elif answer == "2":
            Castle.inside_castle()
            print("You climb the vines and make your way up the castle.")
        else:
            Game.game_over("You got Shrekd")

    def inside_castle():

        print("\nYou sneak your way inside the castle from above")
        print("\nYou spot two giant doors, only one leads to your destination...")
        print("1). Enter the door on the left.")
        print("2). Enter the door on the right.")

        answer = input("> ")

        if answer == "1":
            Game.game_over("I guess you were not right this time.")
        elif answer == "2":
            print("You encounter a mighty dragon!")
            print("How are you going to deal with this dragon?!")
            print("1). Give up and call it quits.")
            print("2). Throw Donkey at the dragon as a 'sacrifice'.")
            print("3). Charge the dragon head-on for 1 on 1 Combat!")

            answer = input("> ")

            if answer == "1":
                Game.game_over("This adventure is too much for you.")
            elif answer == "2":
                print("You grab Donkey and hurl him at the dragon!")
                Game.game_over("What do you get when you throw a donkey at a dragon?  You get a castle :D")
            else:
                print("You begin charging at the dragon at speeds unknown...")
                print("\nYou body-slam the dragon into the wall causing a massive explosion!!!")
                print("\nAs the rubble settles, you notice a secret froom exposed from the explosion")
                Castle.secret_chamber()

    def secret_chamber():
        """
        Final endpoint for the game
        You find the deed to the castle after a riddle
        You evict farquad and donkey falls in love with the dragon?
        """

        print("The chamber seems completely empty, until you spot a lone die on the floor...")
        print("\nAs you pick up the dice you hear a voice whisper...")
        print("\nYou've come this far, the castle is yours...")
        print("\nif you can roll a 6, the entire kingdom will be yours")
        print("\nBut if you roll anything else, your soul is mine!")
        print("\nDo you dare risk it all?")
        print("\n1). Let's risk it all!")
        print("\n2). I'm not greedy.  I'm an ogre.")
        
        answer = input("> ")

        if answer == "1":
            print(dice_roll)
            if dice_roll == 1:
                print("[-------]")
                print("[       ]")
                print("[   O   ]")
                print("[       ]")
                print("[-------]")
                Game.game_over("WHY WOULD YOU RISK IT AND LOSE IT ALL AT THE END?!")
            if dice_roll == 2:
                print("[-------]")
                print("[ 0     ]")
                print("[       ]")
                print("[     0 ]")
                print("[-------]")
                Game.game_over("WHY WOULD YOU RISK IT AND LOSE IT ALL AT THE END?!")
            if dice_roll == 3:
                print("[-------]")
                print("[ O     ]")
                print("[   O   ]")
                print("[     O ]")
                print("[-------]")
                Game.game_over("WHY WOULD YOU RISK IT AND LOSE IT ALL AT THE END?!")
            if dice_roll == 4:
                print("[-------]")
                print("[ O   O ]")
                print("[       ]")
                print("[ O   O ]")
                print("[-------]")
                Game.game_over("WHY WOULD YOU RISK IT AND LOSE IT ALL AT THE END?!")
            if dice_roll == 5:
                print("[-------]")
                print("[ O   O ]")
                print("[   O   ]")
                print("[ O   O ]")
                print("[-------]")
                Game.game_over("WHY WOULD YOU RISK IT AND LOSE IT ALL AT THE END?!")
            if dice_roll == 6:
                print("[-------]")
                print("[ O   O ]")
                print("[ O   O ]")
                print("[ O   O ]")
                print("[-------]")
                Game.game_over("HOLY FARQUAD!  WE WON THE KINGDOM!")
        elif answer == "2":
            Game.game_over("YOU WIN A CASTLE!")     

Game.start()
