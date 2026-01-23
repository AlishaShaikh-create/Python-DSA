# Polymorphism: Polymorphism allows the object of different classes to be treated as object of a common superclass . It provides a way to perform a single action in different forms . Polymorphism is typically achieved through method overriding and interfaces

# Polymorphism means multiple forms


# method overriding :

# method overriding allows a child class to provide a specific implementation of a method that is already defined in the parent class

# base class
class Animal:
    def speak(self):
        return "Sound of the animal"

# Derived class
class Dog(Animal):
    def speak(self):
        return "wooff"    
# Derived class
class Cat(Animal):
    def speak(self):
        return "Meow"
    
## function that demonstrates the polymorphism
def animal_speak(animal):
    print(animal.speak())
    
dog=Dog()
cat=Cat()
print(dog.speak()) # wooff
print(cat.speak()) # Meow

animal_speak(dog) # wooff