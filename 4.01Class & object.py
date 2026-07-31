# Define a class
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}")

# Create objects of Student class
s1 = Student(101, "Harshvardhan")
s2 = Student(102, "Vivek")

# Call methods using objects
s1.display()
s2.display()
