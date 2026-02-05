#for loop

'''for i in range(1,11):
    print("prince")
    
--------------------------------------------------    '''


#conditional statements:

''''a = int(input("enter your age? : "))
if a>=18:
    print("Congrats you are an adult")

else:
    print("oops! you are a minor ")'''
'''-----------------------------------------------------
a = int(input("Enter your marks: "))
if a >= 90:
    print("Wow, your grade is A+ ")   
elif 80 <= a < 90:
    print("YOUR GRADE IS B+")
elif 70 <= a < 80:
    print("YOUR GRADE IS B")
elif a>=60 and a<70:
    print("YOUR GRADE IS C+")
elif 50 <= a < 60:
    print("YOUR GRADE IS C")

else:
    print("OOPS!, YOU FAILED. TRY HARD NEXT TIME ")    

---------------------------------------------------------------------'''

#### Range 
'''for i in range(1,11):
    print(i)   #for simple whole number from 1 to 10 


for i in range(1,11,2):  #(start,end,steps) end is not included
    print(i) #foor printing odd numbers '''

'''for i in range (2,21,2):
    print(i)    #for printing even numbers'''



'''print("THIS IS A PROGRAM TO CALCULATE THE SUM OF THE RANGE OF  GIVEN NUMBERS")
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))
total = 0 
for i in range(a,b+1):
    total = total + i 
     
print(f"Sum of numbers from {a} to {b} is {total}")  '''

'''
scores = [10,20,1,22,36,90,0]
highest = scores[0]
lowest = scores[0]

for i in scores:
    if highest < i:
        highest = i 
print(highest)

for i in scores:
    if lowest > i:
        lowest = i 
print(lowest)       '''


'''num = 1
while num <= 5:
    print(num)
    num=num +1
'''

correct_pass = "prince"

while True:    
    
    passs = str(input("Enter your password: "))
    if passs == correct_pass:
        print("Correct password \n logged in.")
        break
    else:
        print("Wrong password , please try again!!!")
    

         


  







