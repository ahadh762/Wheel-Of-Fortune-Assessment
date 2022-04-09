import random

def Validate_Input(input_type, message):
    valid_input = False
    while valid_input == False:
        if input_type == "name":
            player_name = input(message)
            if any(c.isnumeric() for c in player_name):
                print()
                print("Error: Invalid Name! Only name's with alphabetic characters (A-Z) allowed!\n")
            elif len(player_name) > 20:
                print()
                print("Error: Name is too long! (Enter a name with 20 characters or less!)\n")
            else:
                valid_input == True
                return player_name
        elif input_type == "consonant":
            consonant = input(message)
            if any(c.isnumeric() for c in consonant) or len(consonant) > 1:
                print()
                print("Error: Invalid Input!\n")
            elif consonant not in ['aeiou']:
                print()
                print("Error: Vowel inputted!\n")
            else:
                valid_input == True
                return consonant


def Game_Setup():
    
    global correct_word
    global player_list
    global dict_lines
    global player_1_bank
    global player_2_bank
    global player_3_bank 


    player_1_bank = 0
    player_2_bank = 0
    player_3_bank = 0

    print("\nWelcome to Wheel of Fortune!\n============================\n")

    player_1 = Validate_Input("name",'Enter Name for Player 1: ').title()
    player_2 = Validate_Input("name",'Enter Name for Player 2: ').title()

    while player_2.lower() == player_1.lower():  # Error check for duplicate names
        print()
        print("Error: Name taken! Pick a different name!\n")
        player_2 = Validate_Input("name",'Enter Name for Player 2: ').title()

    player_3 = Validate_Input("name",'Enter Name for Player 3: ').title()  # Error check for duplicate names

    while player_3.lower() == player_1.lower() or player_3.lower() == player_2.lower():
        print()
        print("Error: Name taken! Pick a different name!\n")
        player_3 = Validate_Input("name",'Enter Name for Player 3: ').title()

    player_list = [player_1, player_2, player_3]

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

    print("\nSolve the puzzle:\n")
    print(' '.join(empty_board))
    print()


    

# Function Validate_Guess takes input choice and prompts user for either
# a word (if choice = 0) or a letter (if choice = 1) and ensures they are valid
# Returns the guess (letter or word) and choice (0 or 1)

def Validate_Guess(choice):

    # Ask user to guess a valid word (if invalid prompt them again)
    if choice == 'word':
        guess = input("Guess a word: ").lower()
        print()
        valid_word = guess in dict_lines
        while valid_word == False:
            print(f'Invalid word: "{guess}".', end = ' ')
            guess = input('Guess a word: ').lower()
            print()
            valid_word = guess in dict_lines
        return guess, choice
    
    # Ask user to guess a valid letter (if invalid prompt them again)
    else:
        guess = input("Guess a letter: ").lower()
        print()
        valid_letter = guess.isalpha()
        while (valid_letter == False or len(guess) != 1) :
            print(f'Invalid letter: "{guess}".', end = ' ')
            guess = input('Guess a letter: ').lower()
            print()
            valid_letter = guess.isalpha()
        return guess, choice



def Next_Player():
    return player_list


def Player_Bank(current_player, prize):
    if current_player == 1:
        player_1_bank += prize
    elif current_player == 1:
        player_2_bank += prize
    else:
        player_3_bank += prize


def Spin_Wheel(player, final_round = False):
    if not final_round:
        wheel = ['Lose A Turn!', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankrupt!',\
            750, 800, 300, 200, 100, 500, 400, 300, 200, 850, 700, 200, 150, 450]
        wheel_value = random.choice(wheel)

        if isinstance(wheel_value,int):
            print(f"{player} goes first!\n{player} spins the wheel, and it lands on ${wheel_value}!")
        else:
            print(f"{player} goes first!\n{player} spins the wheel, and it lands on {wheel_value}!")

        return wheel_value


def Round(round_number):
    if round_number == 1:
        current_player = random.choice(player_list)
        wheel_spin = Spin_Wheel(current_player)


        print(current_player)

Game_Setup()
Round(1)
