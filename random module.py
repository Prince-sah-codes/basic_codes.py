import random 
#print(random.random())
#randit
'''print(random.randint(10,20))''' #it prints any random integer number between (a,b) 

#choice
'''a = [1,22,34,21,23,45]
print(random.choice(a))

fruits = [ "apple","banana", "orange", "guava"]
print(random.choice(fruits))'''

#shuffle
'''random.shuffle(fruits)
print(fruits)'''

#####       DICE ROLLING GAME     ######
print("WELCOME TO THE DICE ROLLING GAME......")

while True:
    dice = input("PRESS 'ENTER' TO ROLL AND 'q' TO QUIT THE GAME: ")
    if dice == 'q':
        print("THANKS FOR PLAYING, BYE...")
        break
    elif dice == '':
        roll = random.randint(1,6)
        print(f"YOUR NUMBER IS {roll}")
        
    else:
        print("INVALID INPUT!!!")



