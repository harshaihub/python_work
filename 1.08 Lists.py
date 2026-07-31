# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])   # Output: apple

# Modifying an element
fruits[1] = "mango"
print(fruits)      # Output: ['apple', 'mango', 'cherry']

# Adding a new element
fruits.append("orange")
print(fruits)      # Output: ['apple', 'mango', 'cherry', 'orange']

# Removing an element
fruits.remove("apple")
print(fruits)      # Output: ['mango', 'cherry', 'orange']

# Iterating through the list
for fruit in fruits:
    print(fruit)
