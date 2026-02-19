""""
a = int(input("enter a number="))
b = int(input("enter second no.="))

c = a + b
d = a - b
e = a*b
f = a/b

print("Sum of numbers is:",c)
print("Difference of number is:",d)
print("Product of numbers is:", e)
print("division of numbers is:",f)
"""
"""
print(max(1,2,3,4,5,6))
print(min(65,43,22,41,3))
"""
'''
a = float(input("enter first side="))
b = float(input("enter second side="))
c= float(input("enter third side="))
s = (a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5

print("Semi perimeter of the triange is=",s)
print("Area of the triangle is=",round(area,2))'''

# slicing in strings####

#a = "hello world"
'''
indexing syntax= string[index]
slicing syntax = string[start:end:step]
start: starting from
end:ended to (excluded)
step: step se aage badhna
'''
#print(a[1:11:3])

#fstings in python:

"""name="prince"
language="python"
age= 12
print(f"{name} is {age} years old, he learn {language} daily")"""



"""name = str(input("enter your name:"))
language = str(input("enter your language name:"))
print(f"Hey, {name}! how do you doing. Lets learn {language}. Do you want something to disscuss?")"""

#escape sequences in python 

#\n = new line 
#\t = tab
#\\ = backslash
#\'= inserts a single quote inside a sinle quoted comma 


"""print("hello prince.\n how are you?")
print("prince \t 20")"""

#string operations:
"""a = "we are learning python. python python"
b = "y"
print(a.count(b))
print(a.upper())
print(a.lower())
print(a.startswith("we"))
print(a.endswith("python"))"""




#lists in python 


"""students = ["prince",12, 3.6]
print(f"{students[0]} is a best student in grade {students[1]}. \n he got {students[2]} gpa ")

week = ["sun","mon","tue","wed","thu","fri","sat"]
print(f"the last day of week is {week[6]}")
print(f"the first day of week is {week[0]}")
print(f"there are {len(week)} day in a week")
print(len(week))"""


#count 
"""
a =[0,2,1,2,2,2,2,2,2,2,4,4,4,2,4,3,2,2,3,3,]
print(f"The given lists is:{a}")
b = int(input("Enter the number you wanted to be count:"))
c = a.count(b)
print(f"The occurence of given number in the lists is:{c}")"""

#tuple
"""
t = (1,3,4,"prrr",True,)
print(type(t))"""

#sets in python 

'''a ={1,"ppp",34}
print(type(a))
print(len(a))
------------------------------------------------------------------------------------------'''

#user_defined function:
'''def e_o(number):
    if number % 2 == 0 :
      return "even"
    else:
      return "odd"

a = int(input("enter a number to check even or odd: "))
result = e_o(a)
print(f"the given number is {result}")'''

'''def sum(a,b):
   add = a+b
   return add

val1 = int(input("Enter first number:"))
val2 = int(input("Enter second number:"))

result=sum(val1,val2)  
print(f'Sum of {val1} and {val2} is {result}')/'''

# filter and map 

seq = [1,2,33,6,3,9]
mapped_Output = map(lambda x: "odd" if x% 2 != 0 else "even", seq)
mapp2= map(lambda y: y**2, seq)
print(f"list of odd and even in the given list {seq} is {list(mapped_Output)}")
print(f"list of squuare of the given numbers in the list {seq} is {list(mapp2)}")
