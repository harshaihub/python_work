#🐞 Debugging
#Debugging is about finding and fixing errors in your code.
#Common techniques:
#Print statements → Quick checks of variable values.
#Using pdb (Python Debugger):

import pdb

def divide(a, b):
    pdb.set_trace()   # sets a breakpoint
    return a / b

print(divide(10, 0))

#This lets you step through code line by line.
#IDE tools → VS Code, PyCharm have built-in debuggers with breakpoints.

#✅ Testing with unittest
#Python’s built-in unittest module helps you systematically check your code.

#Example: Testing the Calculator


import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        # Check exception
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    
    unittest.main()
#Key Assertions
#assertEqual(a, b) → checks equality.
#assertTrue(x) / assertFalse(x) → checks boolean.
#assertRaises(Error, func, args) → checks if error is raised.

#🔄 Workflow
#Write code (e.g., calculator functions).
#Write tests in a separate file (e.g., test_calculator.py).
#Run tests:
#bash
#python -m unittest test_calculator.py
#Fix bugs until all tests pass.

#🚀 Why it matters
#Debugging helps you find problems quickly.
#Testing ensures your project stays correct even after changes.
# Together, they make your mini projects professional-grade.