# 5.write class and function for the equation sqrt(x1-x2) ^ 2 + sqrt( y1 – y2 ) ^2 using try except handling

from math import *
try:
  class Sqrt:

      def square_root(self,x1,x2,y1,y2):

        x = (x1-x2)**0.5 ; y= (y1-y2)**0.5
        res = (x**2) + (y**2)
        print(x,y)
        print(res)

  a,b,c,d = float(input("Enter value of X1 :")), float(input("Enter value of X2  :")), float(input("Enter value of y1 :")),float(input("Enter value of y2 :"))
  object = Sqrt()
  object.square_root(a,b,c,d)

except ValueError:
    print("Input to sqrt() function must be non-negative")
