# 2) write a program to create the equation (a+b+c) * (a-b-c) * ab + a^2 + b ^2 + (abc)^3

a,b,c = int(input("Enter value a :")),int(input("Enter value b :")),int(input("Enter value c:"))

print(((a+b+c) * (a-b-c) * (a*b) + (a**2)  + (b**2) + ((a*b*c)**3)))
