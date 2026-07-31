#📘 What are Custom Exceptions?
#Python has many built-in exceptions (ValueError, ZeroDivisionError, etc.).
#Sometimes you need to define your own exception type to handle specific cases in your program.
#You do this by creating a new class that inherits from Exception.

#🧩 Example: Defining a Custom Exception

# Define custom exception
class InvalidAgeError(Exception):
    pass

# Function using custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Access granted")

# Handling custom exception
try:
    check_age(15)
except InvalidAgeError as e:
    print("Custom Exception:", e)


#📘 Example with Multiple Custom Exceptions

class NegativeMarksError(Exception):
    pass

class ExceedMarksError(Exception):
    pass

def validate_marks(marks):
    if marks < 0:
        raise NegativeMarksError("Marks cannot be negative")
    elif marks > 100:
        raise ExceedMarksError("Marks cannot exceed 100")
    else:
        print("Marks are valid:", marks)

try:
    validate_marks(120)
except NegativeMarksError as e:
    print("Error:", e)
except ExceedMarksError as e:
    print("Error:", e)