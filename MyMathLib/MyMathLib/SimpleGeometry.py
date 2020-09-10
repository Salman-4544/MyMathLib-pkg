#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Salman-pc
#
# Created:     08/09/2020
# Copyright:   (c) Salman-pc 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


##area
def SquareArea(A : float):
    print(A*A)

def RectangleArea(long : float,wide :float):
    print(long * wide)

def TriangleArea(base : float,height : float):
    Result = (base*height)* 0.5
    print(Result)

def CircleArea(radius : float):
    Result = 3.14*radius*radius
    print(Result)

def TrapezoidArea(base1 : float,base2 : float,heigth : float):
    Resutl =  0.5*(base1 * base2)*heigth
    print(Resutl)

#perimeter

def SquarePerim(a:float):
    print(a*a*a*a)

def RectPerim(long : float,wide :float):
    result =  long + wide * 2
    print(result)

def CircleCircum(radius:float):
    print(2*3.14*radius)


