class Animal:

    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(prey):
    pass

class Hawk(predator):
    pass

class Fish(prey, predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()
hawk.hunt()