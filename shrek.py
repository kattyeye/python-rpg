
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
                "Fiona asks you a very important question, what's your favorite color? ")
            print(
                "If your answer doesn't meet her requirements, you're done. Hint: Nature...")
            answer = input("> ")
            if answer == "blue" or "green" or "black":
                print(
                    "\nYou fell in love with Fiona, you must go with her to the castle to meet her parents.")
                Castle.castle_start()
            else:
                print(
                    "Nahhhh. Fiona says, 'Byeeeee' and marries your nemesis, Lord Farquaad")
        elif answer == "2":
            Game.game_over("Fiona says, 'Byeeeee' and marries Lord Farquaad")
        else:
            Game.game_over("Better luck next time. Type a number.")


class Swamp:
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
            else:
                print('Donkey says: "Shrek! That isn\'t an option"')

    def riddle1():
        question1 = {
            "What can't you see, but it's always in front of you?": ["Future", "the future", "your future", "time ahead", "future time"]
        }
        for question1, correct_answers in question1.items():
            user_answer = input(f"{question1}: ")
            if any(user_answer.lower() == answer.lower() for answer in correct_answers):
                print("Correct!")
            else:
                print('Donkey says: "Shrek! That isn\'t an option"')

    def swamp_room():

        print('welcome to the swamp')
        print('This swamp is filled with mysterious characters')
        print()
        answer = input('    l or r    --')
        if answer == 'l':

            print('Pinocchio')
            for question, correct_answers in Swamp.questions.items():
                user_answer = input(f"{question}: ")
                if any(user_answer.lower() == answer.lower() for answer in correct_answers):
                    print("Correct!")
                    Swamp.riddle2()
                else:
                    print('Donkey says: "Shrek! That isn\'t an option"')
        elif answer == 'r':
            print(
                'Fairy Godmother appears, flapping her wings as she floats higher into the sky.')
            print('She asks you a riddle, answer to go on.')
            Swamp.riddle1()
        else:
            print('Donkey says: "Shrek! That isn\'t an option"')


class Castle:
    def castle_start():

        print("\nYou slowly approach the bridge to Lord Farquads castle...")
        print("\nYou notice 2 points of entry into the castle.")
        print("\nWhich path do you choose?")
        print("1). Enter through the front gates.")
        print("2). Climb the vines on the side of the castle.")

        answer = input(">")

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

        answer = input(">")

        if answer == "1":
            Game.game_over("Filler text for now...")
        elif answer == "2":
            print("You encounter a mighty dragon!")
            print("How are you going to deal with this dragon?!")
            print("1). Give up and call it quits.")
            print("2). Throw Donkey at the dragon as a 'sacrifice'.")
            print("3). Charge the dragon head-on for 1 on 1 Combat!")

            answer = input(">")

            if answer == "1":
                Game.game_over("Filler text for now...")
            elif answer == "2":
                print("You grab Donkey and hurl him at the dragon!")
            else:
                print("You begin charging at the dragon at speeds unknown...")
                print(
                    "\nYou body-slam the dragon into the wall causing a massive explosion!!!")
                print(
                    "\nAs the rubble settles, you notice a secret froom exposed from the explosion")
                Castle.castle_secret_chamber()

    def castle_secret_chamber():
        """
        Final endpoint for the game
        You find the deed to the castle after a riddle
        You evict farquad and donkey falls in love with the dragon?
        """


Game.start()
