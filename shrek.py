class Player:
    """ This is a class that represents the main character in a game. """

    def __init__(self, name):
        self.name = name

    def printname(self):
        print('Welcome', self.name)


p1 = Player('Shrek')

p1.printname()


def start():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? (l or r)")

    answer = input(">").lower()

    if "l" in answer:
        forest_room()
    elif "r" in answer:
        swamp_room()
    else:
        game_over("Don't you know how to type something properly?")


# start the game


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
            "\nYou fell in love with Fiona, you must go with her to the castle to meet her parents.")
        castle_start()
    elif answer == "2":
        game_over("Fiona says, 'Byeeeee' and marries Lord Farquaad")
    else:
        game_over("Better luck next time. Type a number.")


def swamp_room():

    print('welcome to the swamp')
    print('This swamp is filled with mysterious characters')
    print()
    answer = input('    l or r    --')
    if answer == 'l':
        print('Pinocchio')
        print()
        input('o or p')
        if answer == 'o':
            print()
        elif answer == 'p':
            print()
        else:
            print('Donkey says: "Shrek! That isn\'t an option"')
    elif answer == 'r':
        print('Fairies')
        print()
        input('g or h')
        if answer == 'g':
            print()
        elif answer == 'h':


class Game:

    def start():
        print("\nYou are standing in a large, open field.")
        print("There is a pathway into the woods to your left. To your right, there is a path to the swamp. (l or r)")

        answer = input(">").lower()

        if answer == "l":
            Forest.forest_room()
        elif answer == "r":
            swamp_room()
        else:
            game_over("Type l or r next time.")

    def play_again():
        print("\nDo you want to play again? (y or n)")

        # convert the player's input to lower_case
        answer = input(">").lower()

        if "y" in answer:
            # if player typed "yes" or "y" start the game from the beginning
            start()
        else:
            # if user types anything besides "yes" or "y", exit() the program
            exit()

    def game_over(reason):
        print("\n" + reason)
        print("Game Over!")
        play_again()

    start()
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
                "\nYou fell in love with Fiona, you must go with her to the castle to meet her parents.")
            castle_start()
        elif answer == "2":
            game_over("Fiona says, 'Byeeeee' and marries Lord Farquaad")
        else:
            game_over("Better luck next time. Type a number.")


class Swamp:
    def swamp_room():
        print('welcome to the swamp')
        print('This swamp is filled with mysterious characters')

        input('l or r: ')
        if input == 'l':
            print('Pinocchio')
            print()
            input('o or p')
            if input == 'o':
                print()
            elif input == 'p':
                print()
            else:
                print('Donkey says: "Shrek! That isn\'t an option"')
        elif input == 'r':
            print('Fairies')
            print()
            input('g or h')
            if input == 'g':
                print()
            elif input == 'h':
                print()
            else:
                print('Donkey says: "Shrek! That isn\'t an option"')
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
            game_over("Lord Farquad captured you.  Feels bad man.")
        elif answer == "2":
            inside_castle()
            print("You climb the vines and make your way up the castle.")
        else:
            game_over("You got Shrekd")

    def inside_castle():

        print("\nYou sneak your way inside the castle from above")
        print("\nYou spot two giant doors,")
