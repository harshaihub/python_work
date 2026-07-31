# Program to categorize a number using if, elif, else

num = int(input("Enter a number: "))

# Conditional statements
if num > 0:
    print("The number is positive.")
    
    # Nested condition
    if num % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")

elif num < 0:
    print("The number is negative.")
    
    # Nested condition
    if abs(num) > 10:
        print("Its absolute value is greater than 10.")
    else:
        print("Its absolute value is less than or equal to 10.")

else:
    print("The number is zero.")
