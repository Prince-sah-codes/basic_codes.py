
balance = 0.0
def check_balance():
    
    print(f"YOUR CURRENT BALANCE IS INR:{balance}/-")
    print("-----------------------------------------------------------------------------")

def deposite():
    print("-----------------------------------------------------------------------------")
    depo = int(input("ENTER AMOUNT TO BE DEPOSITED: "))
    if depo < 0: 
        print("CAN'T TAKE NEGATIVE AMOUNT, PLEASE RETRY.")
    else:    
    
        global balance
        
        balance = balance + depo
        print("-----------------------------------------------------------------------------")
        print(f"YOU DEPOSITED INR:{depo}/-\n YOUR CURRENT BALANCE IS INR:{balance}/-") 
        print("-----------------------------------------------------------------------------")

    
    

def withdraw():
    wd = int(input("ENTER AMOUNT YOU WANT TO WITHDRAW: "))
    print("-----------------------------------------------------------------------------")
    global balance
    if wd < 0:
        print("SORRY, PLEASE ENTER POSITIVE VALUE")
        print("-----------------------------------------------------------------------------")
    elif wd > balance:
        print("NO SUFFICIENT BALANCE TO WITHDRAW, PLEASE CHECK THE BALANCE AND RETRY AGAIN")
        print("-----------------------------------------------------------------------------")
    else:        
      
        balance = balance - wd 
        print(f"SUCCESSFULLY WITHDRAWN INR:{wd}/- \n YOUR CURRENT BALANCE IS {balance}")
        print("-----------------------------------------------------------------------------")
        if balance == 0 :
            print("-----------------------------------------------------------------------------")
            print("YOU ARE OUT OF BALANCE, PLEASE DEPOSITE SOME AMOUNT TO CONTINE BANKING")
            print("-----------------------------------------------------------------------------")


print("-----------------------------------------------------------------------------")
print("WELCOME TO PRINCE BANK. WHAT DO YOU WANNA GO WITH?")
print("-----------------------------------------------------------------------------")
while True:
    
    print("1. CHECK YOUR BALANCE ")
    print("2. DEPOSITE AN AMOUNT ")
    print("3. WITHDRAW AMOUNT")
    print("4. QUIT")
    choice = int(input("ENTER YOUR CHOICE BETWEEN(1-4): "))
    print("-----------------------------------------------------------------------------")

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposite()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("QUITING...")
        break 
    else:
        print("INVALID INPUT!!!  TRY AGAIN...")  


print("THANKS FOR USING PRINCE BANKING. HOPE YOU COME BACK LATER!!! ")
print("-----------------------------------------------------------------------------")


    
