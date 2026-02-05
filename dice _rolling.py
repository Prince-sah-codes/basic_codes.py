#####       DICE ROLLING GAME     ######
import random


print("WELCOME TO THE DICE ROLLING GAME......")

while True:
    dice = input("PRESS 'ENTER' TO ROLL THE DICE AND 'q' TO QUIT THE GAME: ")
    dice=dice.strip()
    dice = dice.lower()
    if dice == 'q' :
        print("THANKS FOR PLAYING, BYE...")
        break
    elif dice == '':
        roll = random.randint(1,6)
        print(f"YOUR NUMBER IS {roll}")
        
    else:
        print("INVALID INPUT!!!")