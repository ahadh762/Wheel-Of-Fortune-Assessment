import random


def Game_Setup():
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


def Spin_Wheel(final_round = False):
    if final_round == False:
        wheel = ['Lose A Turn', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankrupt',\
            750, 800, 300, 200, 100, 500, 400, 300, 200, 850, 700, 200, 150, 450]
        wheel_value = random.choice(wheel)
        return wheel_value

print(Spin_Wheel())

print(Game_Setup())