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
a = float(input("enter first side="))
b = float(input("enter second side="))
c= float(input("enter third side="))
s = (a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5

print("Semi perimeter of the triange is=",s)
print("Area of the triangle is=",round(area,2))