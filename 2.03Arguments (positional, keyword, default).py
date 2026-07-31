#1️. Positional Arguments
#Values are passed in order.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling with positional arguments
greet("Harshvardhan", 21)

#2.Keyword Arguments
#Values are passed using parameter names.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Calling with keyword arguments
greet(age=21, name="Harshvardhan")

#3.Default Arguments
#If no value is provided, the default is used.

def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

# Calling with and without age
greet("Harshvardhan")       # Uses default age = 18
greet("Vivek", 22)          # Overrides default
