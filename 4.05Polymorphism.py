#What is Polymorphism?
#Polymorphism means “many forms”.

#In OOP, it allows the same function name or operator to behave differently depending on the context.

#Makes code flexible, reusable, and extensible.

#@ Types of Polymorphism in Python
#1. Compile-Time Polymorphism (Method Overloading / Operator Overloading)
#Python doesn’t support strict method overloading like C++, but you can achieve similar behavior using default arguments or variable-length arguments.
#Operator overloading is supported.

# Example: Operator Overloading

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):   # Overloading + operator
        return Complex(self.real + other.real, self.imag + other.imag)

    def display(self):
        print(f"{self.real} + {self.imag}i")

c1 = Complex(3, 4)
c2 = Complex(1, 2)
c3 = c1 + c2   # Uses overloaded +
c3.display()   # Output: 4 + 6i

#2. Run-Time Polymorphism (Method Overriding)
#Achieved when a child class overrides a method of the parent class.
#Which method runs is decided at runtime.

# Example: Method Overriding
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):   # Overriding
        print("Bark!")

class Cat(Animal):
    def sound(self):   # Overriding
        print("Meow!")

# Runtime decision
animals = [Dog(), Cat()]
for a in animals:
    a.sound()