#What is Encapsulation?
#Encapsulation = Wrapping data (attributes) and methods (functions) together inside a class.

#It also means restricting direct access to some data by using access specifiers.

#Purpose: Data security, controlled access, and abstraction.

#@ Access Specifiers in Python

#Public → Accessible everywhere (default).

#Protected (_variable) → Accessible within class and subclasses (convention).

#Private (__variable) → Accessible only within the class (name mangling).

# Example Program
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no        # Public attribute
        self._marks = 85              # Protected attribute
        self.__password = "abc123"    # Private attribute

    def show(self):
        print(f"Roll No: {self.roll_no}, Marks: {self._marks}")

    def get_password(self):           # Controlled access
        return self.__password

# Create object
s1 = Student(101, "Harshvardhan")

# Public access
print(s1.roll_no)        # ✅ Allowed

# Protected access (by convention, should not be used outside class)
print(s1._marks)         # ⚠️ Possible, but discouraged

# Private access (not directly allowed)
# print(s1.__password)   # ❌ Error

# Access private via method
print(s1.get_password()) # ✅ Allowed → abc123