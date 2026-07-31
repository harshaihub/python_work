
#What is Inheritance?
#Inheritance allows a class (child/derived class) to acquire properties and methods of another class (parent/base class).

#@Types of Inheritance in Python

#1. Single Inheritance
#One child class inherits from one parent class.


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):   # inherits Person
    def display(self):
        print("Name:", self.name)

s1 = Student("Harshvardhan")
s1.display()

#2. Multilevel Inheritance
#Inheritance across multiple levels (chain).

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

class Intern(Student):
    def __init__(self, name, roll, company):
        super().__init__(name, roll)
        self.company = company

i1 = Intern("Vivek", 102, "Microsoft")
print(i1.name, i1.roll, i1.company)

#3. Multiple Inheritance
#Child class inherits from more than one parent class.


class Teacher:
    def __init__(self, subject):
        self.subject = subject

class Sports:
    def __init__(self, game):
        self.game = game

class Student(Teacher, Sports):
    def __init__(self, subject, game, name):
        Teacher.__init__(self, subject)
        Sports.__init__(self, game)
        self.name = name

s1 = Student("Maths", "Cricket", "Shreyas")
print(s1.name, s1.subject, s1.game)

#4. Hierarchical Inheritance
#Multiple child classes inherit from one parent.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def display(self):
        print("Student:", self.name)

class Teacher(Person):
    def display(self):
        print("Teacher:", self.name)

s1 = Student("Sanmet")
t1 = Teacher("Nassar")
s1.display()
t1.display()

#5. Hybrid Inheritance
#Combination of two or more types.


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, empId):
        super().__init__(name)
        self.empId = empId

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

class Intern(Employee, Student):
    def __init__(self, name, empId, roll, company):
        Employee.__init__(self, name, empId)
        Student.__init__(self, name, roll)
        self.company = company

i1 = Intern("Harshvardhan", 201, 101, "Google")
print(i1.name, i1.empId, i1.roll, i1.company)