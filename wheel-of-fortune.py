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
            elif consonant in ['a','e','i','o','u']:
                print()
                print("Error: That's a vowel! \n")
            elif consonant in game_board:
                print()
                print("Error: Letter has been guessed already")
            else:
                valid_input == True
                return consonant
        elif input_type == "option":
            while valid_input == False:
                try:
                    user_input = int(input(message))
                    if user_input > 3 or user_input < 1:
                        print()
                        print('Error: Invalid input!\n')
                    else:
                        valid_value = True
                        return user_input
                except ValueError:
                    print()
                    print("Error: Invalid input!\n")
                    continue        
        elif input_type == "word":
            word = input(message)
            if any(c.isnumeric() for c in word):
                print()
                print("Error: Invalid Input!\n")
            elif word not in dict_lines:
                print()
                print("Error: Not a Word!\n")
            else:
                valid_input == True
                return word


def Game_Setup():
    
    global correct_word
    global player_list
    global dict_lines
    global player_1_bank
    global player_2_bank
    global player_3_bank 
    global game_board


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
    game_board = []

    for letter in correct_word:
        if letter.isalpha():
            game_board.append("_")
        else:
            game_board.append(letter)


    print("\nSolve this puzzle:\n")
    print(' '.join(game_board))
    print()



def Update_Board(input_type, current_player, guess):

    global game_board

    if input_type == 'letter':
        count = 0
        if any(letter in correct_word for letter in guess):
            print("\nCorrect!\n")
            for i in range(0,len(correct_word)):
                if guess == list(correct_word)[i]:
                    count+=1
                    game_board[i] = guess.upper()
        else:
            print("\nIncorrect!\n")
            current_player = Next_Player(current_player)

    elif input_type == "word":
        if guess.lower() == correct_word:
            game_board = list(correct_word)
            print("Correct!\n")
            print("The word was \n")
            return current_player, 1
        else:
            print("Incorrect!\n")
            current_player = Next_Player(current_player)
            return current_player, 0

    print(' '.join(game_board))
    print()
    return current_player, count



def Next_Player(current_player):
    position = player_list.index(current_player)
    if position == 0 or position == 1:
        next_player = player_list[position + 1]
        print(f"{current_player} loses their turn! {next_player} goes next!\n")
    else:
        next_player = player_list[0]
        print(f"{current_player} loses their turn! {next_player} goes next!\n")
    return next_player


def Player_Bank(current_player, prize, count = -1):
    global player_1_bank
    global player_2_bank
    global player_3_bank
    global bank_list

    player = player_list.index(current_player)

    if player == 0:
        player_1_bank += prize*count
        if count == -1:
            player_1_bank = 0
    elif player == 1:
        player_2_bank += prize*count
        if count == -1:
            player_1_bank = 0
    else:
        player_3_bank += prize*count
        if count == -1:
            player_1_bank = 0

    bank_list = [player_1_bank, player_2_bank, player_3_bank]
    print("\nPlayer Totals:\n")

    for i in range(len(bank_list)):
        print(f"{player_list[i]}: ${bank_list[i]}")

    print()


def Spin_Wheel(player, final_round = False):

    if not final_round:
        wheel = ['Lose a Turn!', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankrupt!',\
            750, 800, 300, 200, 100, 500, 400, 300, 200, 850, 700, 200, 150, 450]
        wheel_value = random.choice(wheel)

        if isinstance(wheel_value,int):
            print(f"{player} spins the wheel, and it lands on ${wheel_value}!\n")
        else:
            print(f"{player} spins the wheel, and it lands on {wheel_value}\n")

        return wheel_value


def Round(current_player):

    wheel_spin = Spin_Wheel(current_player)
    if isinstance(wheel_spin,str):
        if wheel_spin == 'Bankrupt!':
            Player_Bank(current_player,0)

        current_player = Next_Player(current_player)
        print(' '.join(game_board))
        print()
        return current_player, False
    else:
        consonant_guess = Validate_Input('consonant','Guess a consonant: ')
        next_player = current_player
        current_player, count = Update_Board('letter', current_player, consonant_guess)
        if next_player == current_player:
            Player_Bank(current_player, wheel_spin, count)
            return current_player, True
        else:
            return current_player, False



def Loop_Round(current_player):
    start_round = False
    while start_round == False:
        current_player, start_round = Round(current_player)


def Options_Menu(current_player):
    global end_round
    print()
    print(f"OK {current_player}! What would you like to do?")
    print("=================================================\n")
    print("1. Solve the Puzzle\n")
    print("2. Buy a Vowel (Lose $250)\n")
    print("3. Spin the Wheel of Fortune!\n")
    option = Validate_Input("option", 'Choose an option: ')
    print()
    if option == 1:
        end_round = True
    if option == 3:
        print()
        print(' '.join(game_board))
        print()
        Loop_Round(current_player)


Game_Setup()


# Round 1
current_player = random.choice(player_list)
print(f"{current_player} goes first!\n")

end_round = False

Loop_Round(current_player)

while end_round == False:
    Options_Menu(current_player)

