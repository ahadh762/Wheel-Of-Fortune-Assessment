import random
import time
from threading import Timer

def Validate_Input(input_type, message, final_round = False):
    global letter_guesses

    valid_input = False

    while not valid_input:
        time.sleep(0.2)
        if input_type == "name":
            player_name = input(message)
            if any(c.isnumeric() for c in player_name) or player_name == "":
                print()
                print("Error: Invalid Name! Only name's with alphabetic characters (A-Z) allowed!\n")
            elif len(player_name) > 20:
                print()
                print("Error: Name is too long! (Enter a name with 20 characters or less!)\n")
            else:
                return player_name
        elif input_type == "consonant" or input_type == "vowel":
            guess = input(message).lower()
            if any(c.isnumeric() for c in guess) or len(guess) > 1 or guess == "":
                print()
                print("Error: Invalid Input!\n")
            elif guess in letter_guesses:
                print()
                guess = guess.upper()
                print(f"Error: {guess} has been guessed already!\n")
            elif input_type == "consonant":
                if guess in ['a','e','i','o','u']:
                    print()
                    print("Error: That's a vowel! \n")
                elif final_round == True and guess in ['r','s','t','l','n']:
                    print("\nError: R-S-T-L-N-E already provided!\n")
                else:
                    letter_guesses.add(guess)
                    return guess
            else:
                if guess not in ['a','e','i','o','u']:
                    print()
                    print("Error: That's a consonant! \n")
                elif final_round == True and guess == 'e':
                    print("\nError: R-S-T-L-N-E already provided!\n")
                else:
                    letter_guesses.add(guess)
                    return guess
        elif input_type == "option":
            while valid_input == False:
                try:
                    user_input = int(input(message))
                    if user_input > 3 or user_input < 1:
                        print()
                        print('Error: Invalid input!\n')
                    else:
                        return user_input
                except ValueError:
                    print()
                    print("Error: Invalid input!\n")
                    continue        
        elif input_type == "word":
            word = input(message).lower()
            if any(c.isnumeric() for c in word):
                print()
                print("Error: Invalid Input!\n")
            elif word not in dict_lines:
                print()
                print("Error: Not a Word!\n")
            else:
                return word


def Game_Setup(same_players = True, final_round = False):
    global correct_word
    global player_list
    global dict_lines
    global player_1_bank
    global player_2_bank
    global player_3_bank 
    global game_board
    global letter_guesses
    global letter_count
    global consonant_count


    if final_round == False:

        player_1_bank = 0
        player_2_bank = 0
        player_3_bank = 0

        consonant_count = 0
        letter_count = 0
        
        if not same_players:
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

        dictionary_set = set()
        letter_guesses = set()

        for line in dict_lines:
            dictionary_set.add(line)

        dictionary_set = dictionary_set - previous_words

        correct_word = random.choice(tuple(dictionary_set))
        previous_words.add(correct_word)
        print(previous_words)
        game_board = []

        for letter in correct_word:
            if letter.isalpha():
                game_board.append("_")
            else:
                game_board.append(letter)


        print("\nSolve this puzzle:\n")
        print(' '.join(game_board))
        print()

    else: 

        f = open('words_alpha.txt')
        dict_lines = f.read().splitlines()
        f.close()

        dictionary_set = set()
        letter_guesses = set()

        for line in dict_lines:
            dictionary_set.add(line)

        dictionary_set = dictionary_set - previous_words

        correct_word = random.choice(tuple(dictionary_set))
        previous_words.add(correct_word)
        print(previous_words)
        
        game_board = []
        
        for letter in correct_word:
            if letter in ['r','s','t','l','n','e']:
                game_board.append(letter.upper())
            else:
                game_board.append('_')

        print(' '.join(game_board))
        print()


def Update_Board(input_type, guess):
    time.sleep(0.2)
    global game_board
    global current_player
    global letter_guesses
    global letter_count

    if input_type == 'letter':
        letter_count = 0
        if any(letter in correct_word for letter in guess):
            print("\nCorrect!\n")
            for i in range(0,len(correct_word)):
                if guess == list(correct_word)[i]:
                    letter_count+=1
                    game_board[i] = guess.upper()
        else:
            print("\nIncorrect!\n")
            Next_Player()

        letter_guesses.add(guess)
    
        print(' '.join(game_board))
        print()

    elif input_type == "word":
        if guess.lower() == correct_word:
            game_board = list(correct_word)
            print("Correct!\n")
            print("The word was \n")

        else:
            print("Incorrect!\n")
            Next_Player()

        print(' '.join(game_board))
        print()
    
    else: 
        for i in range(0,len(correct_word)):
            if guess == list(correct_word)[i]:
                letter_count+=1
                game_board[i] = guess.upper()

    

def Next_Player():
    global current_player

    position = player_list.index(current_player)
    if position == 0 or position == 1:
        current_player = player_list[position + 1]
        print(f"{current_player} goes next!\n")
    else:
        current_player = player_list[0]
        print(f"{current_player} goes next!\n")


def Consonant_Count():
    global game_board
    global correct_word
    global consonant_count

    board = set(''.join(game_board).lower())
    word = set(correct_word)
    remaining_letters = word - board
    consonant_count = 0
    vowels = set('aeiou')
    for i in remaining_letters:
        if i not in vowels:
            consonant_count += 1


def Player_Bank(prize, round_end = False):
    time.sleep(0.2)
    global player_1_bank
    global player_2_bank
    global player_3_bank
    global bank_list
    global letter_count

    player = player_list.index(current_player)

    if player == 0:
        player_1_bank += prize*letter_count
        if prize == 0:
            player_1_bank = 0
    elif player == 1:
        player_2_bank += prize*letter_count
        if prize == 0:
            player_2_bank = 0
    else:
        player_3_bank += prize*letter_count
        if prize == 0:
            player_3_bank = 0

    bank_list = [player_1_bank, player_2_bank, player_3_bank]

    if round_end == False:
        print("\nPlayer Banks:\n===========\n")

    for i in range(len(bank_list)):
        print(f"{player_list[i]}: ${bank_list[i]}")

    print()


def Spin_Wheel(final_round = False):
    global current_player

    if not final_round:
        wheel = ['Lose a Turn!', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankrupt!',\
            750, 800, 300, 200, 100, 500, 400, 300, 200, 850, 700, 200, 150, 450]
        wheel_value = random.choice(wheel)

        if isinstance(wheel_value,int):
            print(f"{current_player} spins the wheel, and it lands on ${wheel_value}!\n")
        else:
            print(f"{current_player} spins the wheel, and it lands on {wheel_value}\n")
    else:
        wheel = [10000,15000,20000,30000,40000,50000,100000]
        wheel_value = random.choice(wheel)

    return wheel_value


def Round():
    global current_player
    global game_board
    global end_round

    wheel_spin = Spin_Wheel()
    if isinstance(wheel_spin,str):
        if wheel_spin == 'Bankrupt!':
            Player_Bank(0)

        Next_Player()
        print(' '.join(game_board))
        print()
        return False
    else:
        consonant_guess = Validate_Input('consonant','Guess a consonant: ')
        next_player = current_player
        Update_Board('letter', consonant_guess)
        if next_player == current_player:
            Player_Bank(wheel_spin)
            return True
        else:
            return False


def Loop_Round():
    global current_player
    end_round = False
    while end_round == False:
        time.sleep(0.1)
        end_round = Round()


def Options_Menu():
    global end_round
    global current_player
    global game_board
    global letter_count
    global correct_word
    global consonant_count
    
    Consonant_Count() # Prevents players from spinning wheel when no consonants left to guess

    print()
    print(f"OK {current_player}! What would you like to do?")
    print("=================================================\n")
    print("1. I'd like to Solve the Puzzle!\n")
    print("2. Buy a Vowel (Lose $250)\n")
    print("3. Spin the Wheel of Fortune!\n")
    option = Validate_Input("option", 'Choose an option: ')
    print()

    if option == 1:
        guess = Validate_Input("word", "Guess a word: ")
        print()

        if guess.lower() == correct_word.lower():
            game_board = list(correct_word.upper())
            print(f"{current_player} wins the round!\n")
            print("The word was ", end = "")
            print(' '.join(game_board))
            end_round = True

        elif consonant_count == 0:
            print("No consonants remain!\n")
            if guess.lower() != correct_word.lower():
                print("Sorry. That is incorrect!\n")
                Next_Player()
                print(' '.join(game_board))
                Options_Menu()
            else:
                print(f"{current_player} wins the round!\n")
                print("The word was ", end = "")
                print(' '.join(game_board))
                end_round = True

        elif '_' not in game_board:
            if guess.lower() != correct_word.lower():
                print("Sorry. That is incorrect!\n")
                Next_Player()
                print(' '.join(game_board))
                Options_Menu()
            else:
                print(f"{current_player} wins the round!\n")
                print("The word was ", end = "")
                print(' '.join(game_board))
                end_round = True
        
        else:
            print("Sorry. That is incorrect!\n")
            print(' '.join(game_board))
            print()
            Next_Player()
            Loop_Round()

    elif option == 2:
        player = player_list.index(current_player)
        vowels = set('aeiou')
        if bank_list[player] < 250:
            print()
            print("Error: Not enough money to buy a vowel!\n")
        elif vowels.issubset(letter_guesses):
            print()
            print("Error: No vowels left!\n")
        elif '_' not in game_board:
            print()
            print("Error: Board is full!\n")
        else:
            letter_count = -1
            Player_Bank(250)
            vowel = Validate_Input("vowel", "Buy a vowel: ")
            next_player = current_player
            Update_Board('letter',vowel)
            if consonant_count == 0:
                print('No more consonants left!\n')

            elif next_player != current_player:
                Loop_Round()

    else:
        if '_' not in game_board:
            print()
            print("Error: Board is full!\n")
        elif consonant_count == 0:
            print('No more consonants left!\n')
        else:   
            print()
            print(' '.join(game_board))
            print()
            Loop_Round()


def exit():
    print()
    print("\nTimes Up!\n")


previous_words = set()


# Round 1

Game_Setup(same_players = False)
print("\nRound 1:\n==========")
print("Starting player chosen randomly.\n")
current_player = random.choice(player_list)
print(f"{current_player} goes first!\n")

end_round = False

Loop_Round()

while end_round == False:
    time.sleep(0.1)
    Options_Menu()

time.sleep(0.2)
print(f"\n{current_player} gets $1000 added to their winnings!\n")
time.sleep(0.2)
print("\nRound 1 Winnings:\n=================")

count = 1
Player_Bank(1000,round_end = True)

round_1_winnings = bank_list


# Round 2
time.sleep(0.5)
print("\nRound 2:\n==========")
time.sleep(0.2)
print(f"Since {current_player} won the last round. They go first!\n")
Game_Setup(same_players = True)

end_round = False

Loop_Round()

while end_round == False:
    time.sleep(0.1)
    Options_Menu()

time.sleep(0.2)
print(f"\n{current_player} gets $1000 added to their winnings!\n")
time.sleep(0.2)
print("\nRound 2 Winnings:\n=================")

letter_count = 1
Player_Bank(1000,round_end = True)

round_2_winnings = bank_list


# Find winner across all 3 rounds
total_winnings = []

for i in range(len(round_1_winnings)):
    total_winnings.append(round_1_winnings[i] + round_2_winnings[i])

max_winnings = max(total_winnings)
winner = total_winnings.index(max_winnings)
overall_winner = player_list[winner]
current_player = overall_winner


# Show Overall Winnings for each player across both rounds
time.sleep(0.2)
print("\nOverall Winnings:\n=================\n")
for i in range(len(total_winnings)):
    time.sleep(0.2)
    print(f"{player_list[i]}: ${total_winnings[i]}")

print(f"\n{overall_winner} has the most money with ${max_winnings}!\n")
print("They will advance to the Final Round!\n")

time.sleep(0.1)
print("\nFinal Round:\n============\n")
print(f"Welcome to the Final Round, {overall_winner}!")
print("You've spun the mystery prize wheel.\nShould you solve the Final Puzzle, it's yours.\n")
time.sleep(0.1)
print("The letters R-S-T-L-N-E will be revealed for you.\n")


Game_Setup(same_players = False, final_round = True)
mystery_prize = Spin_Wheel(final_round = True)
print("You are allowed to guess 3 consonants and 1 vowel. Enter them now.\n")

consonant_1 = Validate_Input('consonant', "Enter the 1st consonant: ", final_round = True)

Update_Board('final_round', consonant_1)
consonant_2 = Validate_Input('consonant', "Enter the 2nd consonant: ", final_round = True)

Update_Board('final_round', consonant_2)
consonant_3 = Validate_Input('consonant', "Enter the 3rd consonant: ", final_round = True)

Update_Board('final_round', consonant_3)
vowel_1 = Validate_Input('vowel', "Enter a vowel: ")

Update_Board('final_round', vowel_1)


input("\n You will have 10 seconds to solve the puzzle. When you're ready. Press [Enter] to continue. ")

print(' '.join(game_board))

print(f"\n Alright. {current_player}. You have 10 seconds. Good luck!:\n")

solved = False

input_time = 10
t = Timer(input_time, exit)

t.start()

while not solved:
    guess = input("Guess a word: ")
    if guess.lower() == correct_word.lower():
        game_board = list(correct_word)
        print("Correct!\n")
        print("The word was \n")
        print(' '.join(game_board))
        solved = True
        
t.cancel()
