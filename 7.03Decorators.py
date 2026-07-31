#📘 What is a Decorator?
#A decorator is a function that modifies the behavior of another function or method without changing its code.
#It uses the @decorator_name syntax placed above the function definition.
#Commonly used for logging, authentication, timing, and code reuse.
#🧩 Basic Decorator Example

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def greet():
    print("Hello Harshvardhan!")
greet()

#📘 Decorator with Arguments
def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Error: Division by zero not allowed!")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    print("Result:", a / b)

divide(10, 2)   # ✅ Result: 5.0
divide(10, 0)   # ❌ Error handled

#📘 Built-in Decorators
#@staticmethod → Defines a method that doesn’t need self.
#@classmethod → Defines a method that takes cls instead of self.
#@property → Defines getter/setter for attributes.
#Example:

class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):   # getter
        return self._name

    @name.setter
    def name(self, value):   # setter
        self._name = value

s = Student("Harshvardhan")
print(s.name)   # Getter → Harshvardhan
s.name = "Vivek" # Setter
print(s.name)   # Vivek