# 7)  Using class and function - Write a program for palindrome Ex. Madam


class Palindrome:

    def checker(self,value):
         compare = value[::-1]
         if value == compare:
             return f"The given Value {value} is a palindrome"
         else :
             return f"The given Value {value} is not a palindrome"


value = input("Enter The Value :")
object = Palindrome()
x = object.checker(value)
print(x)
