class Animal:
    def __init__ (self, name, health):
        self.name = name
        self.health = health
    def make_sound(self):
        print (f"{self.name} издает звук")
    def info(self):
        print(f"{self.name}, здоровье: {self.health}")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} лает: Гав!")

class Cat(Animal):
    def __init__(self, name, health, is_lazy):
        super().__init__(name, health)
        self.is_lazy = is_lazy
    def make_sound(self):
        if self.is_lazy:
            print(f"{self.name} слишком ленив, что бы мяукать")
        else:
            print(f"{self.name} мяукает: Мяу!")

myDog = Dog("Neon", 100)
myCat = Cat("Bee", 100, True)
hisCat = Cat("Bea", 100, False)

myDog.make_sound()
myCat.make_sound()
hisCat.make_sound()