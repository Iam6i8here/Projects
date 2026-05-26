print(r'''
    ********************************************************************************
                        ____...------------...____
                   _.-"` /o/__ ____ __ __  __ \o\_`"-._
                 .'     / /                    \ \     '.
                 |=====/o/======================\o\=====|
                 |____/_/________..____..________\_\____|
                 /   _/ \_     <_o#\__/#o_>     _/ \_   \
                 \_________\####/_________/
                  |===\!/========================\!/===|
                  |   |=|          .---.         |=|   |
                  |===|o|=========/     \========|o|===|
                  |   | |         \() ()/        | |   |
                  |===|o|======{'-.) A (.-'}=====|o|===|
                  | __/ \__     '-.\uuu/.-'    __/ \__ |
                  |==== .'.'^'.'.====|
              jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
                  `""""-""""""""""""""""""""""""""-""""`
    ********************************************************************************
    ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    "You're at a cross road. "
    "Where do you want to go? "
    "Type 'left' or 'right'.\n")

if choice1 == "left":

    choice2 = input(
        "You've come to a lake. "
        "Type 'wait' to wait for a boat. "
        "Type 'swim' to swim across.\n"
    )

    if choice2 == "wait":

        choice3 = input(
            "You arrive at the island unharmed. "
            "There is a house with 3 doors. "
            "One red, one yellow and one blue. "
            "Which colour do you choose?\n"
        )

        if choice3 == "red":
            print("The room was full of fire. Game Over!")

        elif choice3 == "blue":
            print("The room was full of beasts. Game Over!")

        elif choice3 == "yellow":
            print("You found the treasure. Congratulations! You Win!")

        else:
            print("Invalid choice. Game Over!")

    else:
        print("You get attacked by an angry trout. Game Over!")

else:
    print("You fell into a hole. Game Over!")
