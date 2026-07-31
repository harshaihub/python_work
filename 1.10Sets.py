# Creating a set
numbers = {1, 2, 3, 4, 4, 5}

print(numbers)  
# Output: {1, 2, 3, 4, 5}  # duplicate 4 is removed

# Adding an element
numbers.add(6)
print(numbers)  
# Output: {1, 2, 3, 4, 5, 6}

# Removing an element
numbers.remove(3)
print(numbers)  
# Output: {1, 2, 4, 5, 6}

# Checking membership
print(2 in numbers)   # Output: True
print(10 in numbers)  # Output: False

# Set operations
evens = {2, 4, 6, 8}
print(numbers.union(evens))       # Output: {1, 2, 4, 5, 6, 8}
print(numbers.intersection(evens))# Output: {2, 4, 6}
