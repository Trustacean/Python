from math import pi
class Circle():
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
    def perimeter(self):
        return pi * 2 * self.r
    def area(self):
        return pi * self.r**2
    