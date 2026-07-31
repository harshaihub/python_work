# Combined Example: Input and Output in Python

# Taking multiple inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks1, marks2, marks3 = map(int, input("Enter marks in 3 subjects separated by space: ").split())

# Processing data
average = (marks1 + marks2 + marks3) / 3

# Displaying output with different styles
print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)
print("Marks:", marks1, marks2, marks3, sep=", ")
print("Average Marks = {:.2f}".format(average))   # formatted output
print(f"{name} scored an average of {average:.2f} marks.")  # f-string output
