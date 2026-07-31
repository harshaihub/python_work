# Demonstrating multiple operators in one program

# Arithmetic Operators
a = 10
b = 3
sum_val = a + b        # Addition
prod_val = a * b       # Multiplication
div_val = a / b        # Division

# Relational Operators
is_greater = a > b     # Greater than
is_equal = a == b      # Equality check

# Logical Operators
x = True
y = False
logic_and = x and y    # AND
logic_or = x or y      # OR

# Assignment Operators
c = 5
c += 2   # Equivalent to c = c + 2
c *= 3   # Equivalent to c = c * 3

# Membership Operators
my_list = [1, 2, 3, 4, 5]
check_member = 3 in my_list      # True
check_not_member = 10 not in my_list  # True

# Identity Operators
p = [1, 2, 3]
q = [1, 2, 3]
r = p
identity_check1 = p is q   # False (different objects)
identity_check2 = p is r   # True (same object)

# Output results
print("Arithmetic:", sum_val, prod_val, div_val)
print("Relational:", is_greater, is_equal)
print("Logical:", logic_and, logic_or)
print("Assignment result:", c)
print("Membership:", check_member, check_not_member)
print("Identity:", identity_check1, identity_check2)
