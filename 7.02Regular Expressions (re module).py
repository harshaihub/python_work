#📘 What are Regular Expressions?
#Regular Expressions (Regex) are patterns used to match strings.
#Python provides the re module to work with regex.
#Useful for searching, validating, and manipulating text.

#| Function | Purpose | Example |
#| ``re.match()`` | Checks if pattern matches at **start** of string | ``re.match("Hello", ``"Hello ``World")`` |
#| ``re.search()`` | Finds pattern **anywhere** in string | ``re.search("World", ``"Hello ``World")`` |
#| ``re.findall()`` | Returns **all matches** as a list | ``re.findall("\\d", ``"Roll ``101, ``Marks ``88")`` |
#| ``re.sub()`` | Replaces matches with new text | ``re.sub("\\d", ``"#", ``"Roll ``101")`` |
#| ``re.split()`` | Splits string by pattern | ``re.split("\\s", ``"Hello ``Harshvardhan")`` |

import re

text = "Roll No: 101, Name: Harshvardhan, Marks: 88"

# Match digits
digits = re.findall(r"\d+", text)
print("Digits:", digits)

# Search for name
name = re.search(r"Harshvardhan", text)
if name:
    print("Name found:", name.group())

# Replace marks with 'XX'
new_text = re.sub(r"\d+", "XX", text)
print("Modified:", new_text)


#📘 Common Regex Patterns
#\d → Digit (0–9)

#\w → Word character (letters, digits, underscore)

#\s → Whitespace

# . → Any character except newline

#^ → Start of string

#$ → End of string

#+ → One or more

#* → Zero or more

#{n} → Exactly n times