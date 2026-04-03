#create a password hacking code
import itertools
realpass = str(input("enter your pass: "))
tryy = "1234567890"
for guess in itertools.product(tryy,repeat=len(realpass)):
    guess = ''.join(guess)
   

    if guess == realpass:
        print("pass cracked:",guess)
        break




