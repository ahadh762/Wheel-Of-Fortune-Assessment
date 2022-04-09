import random

def Validate_Input(input_type, message):
    valid_input = False
    if input_type == "name":
        while valid_input == False:
            player_name = input(message)
            if any(c.isnumeric() for c in player_name):
                print()
                print("Error: Invalid Name! Only name's with alphabetic characters (A-Z) allowed!\n")
            elif len(player_name) > 20:
                print()
                print("Error: Name is too long!\n")
            else:
                valid_input == True
                return player_name



def Game_Setup():
    print("Welcome to Wheel of Fortune!\n============================\n")

    Player_1 = Validate_Input("name",'Enter Name for Player 1: ').title()
    Player_2 = Validate_Input("name",'Enter Name for Player 2: ').title()

    while Player_2.lower() == Player_1.lower():
        print()
        print("Error: Name taken!\n")
        Player_2 = Validate_Input("name",'Enter Name for Player 2: ').title()

    Player_3 = Validate_Input("name",'Enter Name for Player 3: ').title()

    while Player_3.lower() == Player_1.lower() or Player_3.lower() == Player_2.lower():
        print()
        print("Error: Name taken!\n")
        Player_3 = Validate_Input("name",'Enter Name for Player 3: ').title()


    f = open('words_alpha.txt')
    dict_lines = f.read().splitlines()
    f.close()
    correct_word = random.choice(dict_lines)
    empty_board = []

    for letter in correct_word:
        if letter.isalpha():
            empty_board.append("_")
        else:
            empty_board.append(letter)

    empty_board = ' '.join(empty_board)


    return empty_board


def Player_Bank(prize):
    print(prize)


def Spin_Wheel(final_round = False):
    if not final_round:
        wheel = ['Lose A Turn', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankrupt',\
            750, 800, 300, 200, 100, 500, 400, 300, 200, 850, 700, 200, 150, 450]
        wheel_value = random.choice(wheel)
        return wheel_value


print(Spin_Wheel())

print(Game_Setup())