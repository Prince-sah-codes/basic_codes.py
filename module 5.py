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

a ={1,"ppp",34}
print(type(a))
print(len(a))
