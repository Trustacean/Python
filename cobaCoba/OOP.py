
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def perimeter(self):
        return 2 * self.width + 2 * self.length
    def area(self):
        return self.width * self.length
    def __str__(self):
        return f"width: {self.width}, length: {self.length}"

class Cube:
    def __init__(self):
        width = int(input("masukkan lebar "))
        length = int(input("masukkan panjang "))
        self.height = int(input("masukkan tinggi "))
        self.base=Rectangle(width, length)
        
    def volume(self):
        return self.base.area()*self.height
    
rectangle1 = Rectangle(20,10)
print(rectangle1)
print(rectangle1.perimeter())
print(rectangle1.area())
cube1 = Cube()

print (cube1.volume())