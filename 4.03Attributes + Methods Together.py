class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

# Create object
s1 = Student(101, "Harshvardhan", 88)

# Access attributes
print(s1.name)   # Output: Harshvardhan

# Call methods
s1.display()     # Output: Roll No: 101, Name: Harshvardhan, Marks: 88
print(s1.grade()) # Output: B
