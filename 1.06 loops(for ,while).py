# Combined Example: For + While Loop

numbers = [3, 5, 7]   # list of numbers

for num in numbers:   # outer loop
    print(f"\nCalculating factorial of {num}:")
    
    fact = 1
    i = 1
    
    # inner while loop
    while i <= num:
        fact *= i
        i += 1
    
    print(f"Factorial of {num} = {fact}")
