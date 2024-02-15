class Animal:
    def speak(self):
        print("Animal Speaking")

#child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("Dog Barking")

class Cat(Dog):
    def meow(self):
        print("Cat Meowing")

#creating object of the class Animal
a = Animal()
#creating object of the class Dog
d = Dog()
d.bark()
d.speak()
#creating object of the class Cat
c = Cat()
c.speak()
c.meow()
c.bark()

#hey , co-pilot please explain what a class is:
