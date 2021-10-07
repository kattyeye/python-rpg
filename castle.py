def castle_start()

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

def inside_castle()
    
    print("\nYou sneak your way inside the castle from above")
    print("\nYou spot two giant doors,")