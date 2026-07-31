#1. try
#Block of code where you expect an exception might occur.

 try:
    x = 10 / 0   # risky code
    
#2. except
#Handles the exception if it occurs.

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero not allowed!")


#3. finally
#Block that always executes, whether an exception occurs or not.
#Used for cleanup tasks (like closing files, releasing resources).

try:
    f = open("demo.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Closing file operation...")
    
#4. raise
#Used to manually trigger an exception.

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    else:
        print("Access granted")

try:
    check_age(15)
except ValueError as e:
    print("Exception:", e)
