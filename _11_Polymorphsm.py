from random import randint

class Shape:
    def Area(self):
        raise NotImplemented
    
    def Perimeter(self):
        raise NotImplemented
    
PI = 22/7

class Circle:
    # def __new__(cls):
    #     return super().__new__()

    def __init__(self, radius):
        self.mRadius = radius

    def SetRad(self, radius):
        self.mRadius = radius

    def Area(self):
        return PI * self.mRadius * self.mRadius
    
    def Perimeter(self):
        return 2 * PI * self.mRadius
    

class Rectangle:
    def __init__(self, base, height):
        self.mBase = base
        self.mHeight = height

    def Area(self):
        return self.mBase * self.mHeight
    
    def Perimeter(self):
        return 2 * self.mHeight * self.mBase
 

#----------------------------------

c1 = Circle(10)
c1.SetRad(7)
print(f"{c1.Area() = }")

r1 = Rectangle(4, 5)
print(f"{r1.Area()=}")
print(f"{r1.Perimeter()=}")

def Area(ref: Shape):
    print(type(ref), ref.Area())

Area(r1)
Area(c1)

lst = [r1, c1]

Area(lst[randint(0, 1)])
