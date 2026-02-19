import random

print("WELCOME TO THE NUMBER GUESSING GAME. WE HAVE A NUMBER THAT NEED TO BE GUESSED. YOU HAVE ONLY 5 CHANCES TO GUESS")
print("SO LETS START THE GAME,")
print("THE NUMBER IS BETWEEN 1 TO 20")

correct_guess = 15

while True:
         
    for i in range(5,0,-1):
        
        print(f"YOU HAVE {i} CHANCE LEFT")
        guess =int(input("ENTER YOUR GUESSED NUMBER: "))
        if guess == correct_guess:
            print("WOW!!! YOU GUESS THE RIGHT NUMBER... THANKS FOR PLAYING \n GAME OVER!!!")
            break
       
        else:
            if guess < correct_guess:
                hl = "HIGHER NUMBER"

            else:
                hl = "LOWER NUMBER"    
            print(f"OOPS YOUR GUESS IS WRONG. TRY {hl}")
        if i == 1:
            print("OOPS YOU ARE OUT OF CHANCES....RETRY AGAIN")
            print(f"THE SECRET NUMBER WAS {correct_guess}")
            break   
    break           

