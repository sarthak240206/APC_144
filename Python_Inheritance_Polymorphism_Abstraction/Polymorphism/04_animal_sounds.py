class Animal:
    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


class Cow(Animal):
    def sound(self):
        print("Moo!")


class Lion(Animal):
    def sound(self):
        print("Roar!")


for animal in [Dog(), Cat(), Cow(), Lion()]:
    animal.sound()
