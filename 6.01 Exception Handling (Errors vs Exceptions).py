#📘 Errors vs Exceptions Recap
#Errors → Mistakes in code (like syntax issues) that stop the program before it runs.

#Exceptions → Runtime problems (like dividing by zero, missing files) that can be handled gracefully.

#🧩 Example 1: Error (Syntax Error)

# Error: Missing colon → program won’t run

if True
    print("Hello Harshvardhan")
    
#👉 This is a syntax error. The program won’t even start until you fix it.

#🧩 Example 2: Exception (Handled with try-except)

try:
    num = 10 / 0   # ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero not allowed!")


#🧩 Example 3: File Handling Exception

try:
    f = open("demo.txt", "r")   # File may not exist
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: File not found.")

#👉 If demo.txt doesn’t exist, the program prints a friendly message instead of crashing.