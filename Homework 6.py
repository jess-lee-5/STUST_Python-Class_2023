# MyShape
class ShapeCalculator:
    def __init__(self, square_side, length, width, radius):
        self.square_side = square_side
        self.length = length
        self.width = width
        self.radius = radius
    
    def getSquareArea(self):
        return self.square_side ** 2
    
    def getRectangleArea(self):
        return self.length * self.width
    
    def getCircleArea(self):
        return 3.14159 * (self.radius ** 2)
        
calculator = ShapeCalculator(square_side=5, length=6, width=4, radius=3)

square_area = calculator.getSquareArea()
rectangle_area = calculator.getRectangleArea()
circle_area = calculator.getCircleArea()

print(f"Square Area: {square_area}")
print(f"Rectangle Area: {rectangle_area}")
print(f"Circle Area: {circle_area}")

# Class Methods (Functions)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nAge = {self.age}"

p1 = Person("John", 36)
p2 = Person("LeBron", 40)
p3 = Person("Kobe", 35)

print(p1)
print(p2)
print(p3)