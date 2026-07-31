# Creating a dictionary
student = {
    "name": "Harsh",
    "age": 21,
    "course": "Business Analytics"
}

# Accessing values using keys
print(student["name"])   # Output: Harsh
print(student["age"])    # Output: 21

# Modifying a value
student["age"] = 22
print(student)  
# Output: {'name': 'Harsh', 'age': 22, 'course': 'Business Analytics'}

# Adding a new key-value pair
student["grade"] = "A"
print(student)  
# Output: {'name': 'Harsh', 'age': 22, 'course': 'Business Analytics', 'grade': 'A'}

# Removing a key-value pair
del student["course"]
print(student)  
# Output: {'name': 'Harsh', 'age': 22, 'grade': 'A'}

# Iterating through dictionary
for key, value in student.items():
    print(key, ":", value)
