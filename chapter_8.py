
#! ----- Chapter 8 - Class and Object -----

#? Class
from vehicle import Vehicle

vehicle1 = Vehicle("Tesla","S Palid","Red",True)
vehicle2= Vehicle("Audi","R8","Black",False)
vehicle3= Vehicle("Porche","911","Green",False)

#? Inheritence

class Animal:
    def __init__(self,name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass

class Cat(Animal,Dog):
    pass

dog = Dog("Bob")
cat = Cat("Sadie")
print(dog.name)
print(dog.isAlive)
print(cat.name)
print(cat.isAlive)