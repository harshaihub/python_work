def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120

print (factorial(20)) #Output  : 243202008176640000

print (factorial(25)) #Output  : 15511210043330985984000000n