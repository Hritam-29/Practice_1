'''# Single Inheritance
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age=age

    def display_name(self):
        print(f"Dog's Name: {self.name}")
    
    def display_age(self):
        print(f"Dog's Age : {self.age}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

# Example Usage
lab = Labrador("Buddy",10)
lab.display_name()
lab.sound()
lab.display_age()

guide_dog = GuideDog("Max",8)
guide_dog.display_name()
guide_dog.guide()
guide_dog.display_age()

retriever = GoldenRetriever("Charlie",6)
retriever.display_name()
retriever.greet()
retriever.sound()'''

# Method Overriding
# We start with a base class and then a subclass that "overrides" the speak method.
class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"

#print(Dog().speak())

# 2 Duck Typing
class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    # This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()

print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))
