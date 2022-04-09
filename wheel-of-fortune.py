import random

def Spin_Wheel(final_round = False):
    if final_round == False:
        wheel = ['Lose A Turn', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankrupt',\
            750, 800, 300, 200, 100, 500, 400, 300, 200, 850, 700, 200, 150, 450]
        wheel_value = random.choice(wheel)
        return wheel_value

print(Spin_Wheel())