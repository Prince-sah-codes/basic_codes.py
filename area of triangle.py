print("THIS IS FOR SCALENE TRIANGLE ")

a = float(input("enter first side="))
b = float(input("enter second side="))
c= float(input("enter third side="))
s = (a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5

print("Semi perimeter of the triange is=",s)
print("Area of scalene triangle is=",round(area,2))

print("THIS IS FOR RIGHT ANGLED TRIANGLE")

a =int(input("enter height of triangle:"))
b =int(input("enter base of triangle:"))
area = 0.5* a*b
print("Area of right angled triangle:", area)