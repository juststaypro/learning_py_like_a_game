class pet:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger
    def petHunger(self):
        if 5 > self.hunger > 0:
            self.hunger -= self.hunger
            print (f"Питомец {self.name} голоден. Сытость {self.hunger}")
        elif self.hunger >= 5:
            self.hunger -= 5
            print (f"Питомец {self.name} проголодался. Сытость {self.hunger}")
        else: 
            self.hunger = 0
            print (f"Питомец {self.name} голодает. Сытость {self.hunger}")
    def toFeed(self):
        if self.hunger > 95:
            print (f"Питомец {self.name} сыт. Не притронулся к пище. Сытость {hunger}")
        elif self.hunger < 95:
            self.hunger += 10
            print (f"Питомец {self.name} покушал. Голод {self.hunger}")

myPet1 = pet("Mot", 50)
hisPet1 = pet("Asik", 50)

myPet1.petHunger()
hisPet1.toFeed()

print (f"Голод моего питомца: {myPet1.hunger}")
print (f"Голод его питомца: {hisPet1.hunger}")