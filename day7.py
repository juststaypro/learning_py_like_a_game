from abc import ABC, abstractmethod
import math
from dataclasses import dataclass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        self.shape = math.pi * self.radius ** 2
        print(f"Площадь круга: {self.shape}")

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        self.shape = self.a * self.b
        print(f"Площадь прямоугольника равна: {self.shape}")

# tester = Shape()
circle = Circle(10)
rectangle = Rectangle(3,4)

circle.area()
rectangle.area()

@dataclass
class Point:
    x: int
    y: int

first = Point(1,2)
second = Point(2,1)

print(first)
print(second)

class Engine():
    def __init__(self, power):
        self.power = power
    def start(self):
        print(f"Двигатель мощностью {self.power} запущен")

class Car():
    def __init__(self,brand):
        self.brand = brand
        self.engine = Engine(1.4)
    def drive(self):
        self.engine.start()
        print(f"{self.brand} едет")

myCar = Car("mitsu")

myCar.drive()
