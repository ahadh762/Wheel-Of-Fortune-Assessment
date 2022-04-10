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

    if input_type == 'letter':
        count = 0
        if any(letter in correct_word for letter in guess):
            print("Correct!\n")
            for i in range(0,len(correct_word)):
                if guess == list(correct_word)[i]:
                    count+=1
                    game_board[i] = guess
        else:
            print("Incorrect!\n")
            current_player = Next_Player(current_player)
    
    print(' '.join(game_board))
    return current_player, count



def Next_Player(current_player):
    position = player_list.index(current_player)
    if position == 0 or position == 1:
        print(f"{current_player} loses their turn!\n")
        next_player = player_list[position + 1]
        print(f"{next_player} goes next!\n")
    else:
        print(f"{current_player} loses their turn!\n")
        next_player = player_list[0]
        print(f"{next_player} goes next!\n")
    return next_player


def Player_Bank(current_player, prize, count):
    global player_1_bank
    global player_2_bank
    global player_3_bank

    player = player_list.index(current_player)

    if player == 0:
        player_1_bank += prize*count
    elif player == 1:
        player_2_bank += prize*count
    else:
        player_3_bank += prize*count

    print("\nPlayer Totals:")
    print(f"{player_list[0]}: ${player_1_bank}")
    print(f"{player_list[1]}: ${player_2_bank}")
    print(f"{player_list[2]}: ${player_3_bank}")


def Spin_Wheel(player, final_round = False):
    if not final_round:
        wheel = ['Lose a Turn!', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankrupt!',\
            750, 800, 300, 200, 100, 500, 400, 300, 200, 850, 700, 200, 150, 450]
        wheel_value = random.choice(wheel)

        if isinstance(wheel_value,int):
            print(f"{player} spins the wheel, and it lands on ${wheel_value}!")
        else:
            print(f"{player} spins the wheel, and it lands on {wheel_value}")

        return wheel_value

def Round_Start(current_player):
    wheel_spin = Spin_Wheel(current_player)
    if isinstance(wheel_spin,str):
        current_player = Next_Player(current_player)
        return current_player, False, wheel_spin
    else:
        consonant_guess = Validate_Input('consonant','Guess a consonant: ')
        next_player = current_player
        current_player, count = Update_Board('letter', current_player, consonant_guess)
        if next_player == current_player:
            Player_Bank(current_player, wheel_spin, count)
            return current_player, True
        else:
            return current_player, False
        
# def Round(current_player):


#     keep_going = True
    
#     while keep_going == True:
#     puzzle_solved = True

#     return current_player, puzzle_solved


Game_Setup()

solved = False

# Round 1
current_player = random.choice(player_list)
print(f"{current_player} goes first!\n")

start_round = False

while start_round == False:
    current_player, start_round = Round_Start(current_player)


# while solved == False:
#     current_player, solved = Round(current_player)

