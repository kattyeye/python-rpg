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
start()


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
