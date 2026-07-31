class Student:
    def __init__(self, roll_no, name):   # Constructor
        self.roll_no = roll_no
        self.name = name

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}")

# Creating objects → constructor is called automatically
s1 = Student(101, "Harshvardhan")
s2 = Student(102, "Vivek")

s1.display()
s2.display()
