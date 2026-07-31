# Defining a function
def greet(name):
    """This function greets the person passed as an argument."""
    return f"Hello, {name}! Welcome to Python."

# Calling the function
print(greet("Harsh"))
print(greet("Vivek"))

# Function with multiple parameters
def add_numbers(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# Calling the function
result = add_numbers(10, 20)
print("Sum:", result)
