# Creating a tuple
student = ("Harsh", 21, "Business Analytics")

# Accessing elements
print(student[0])   # Output: Harsh
print(student[1])   # Output: 21

# Iterating through tuple
for item in student:
    print(item)

# Tuple unpacking
name, age, course = student
print(name)   # Output: Harsh
print(age)    # Output: 21
print(course) # Output: Business Analytics
