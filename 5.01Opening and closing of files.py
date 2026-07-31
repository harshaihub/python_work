#Opening Files
#Use the built-in open() function.

#Syntax:
# file_object = open("filename", "mode")
#Modes:

#"r" → Read (default)

#"w" → Write (creates new file or overwrites existing)

#"a" → Append (adds data at end)

#"b" → Binary mode (e.g., "rb", "wb")

#"r+" → Read & Write

#Closing Files
#Use close() method to release resources.

#Ensures all buffered data is written to disk.

# Example Program


# Opening a file in write mode
f = open("demo.txt", "w")
f.write("Hello Harshvardhan!\n")
f.write("This is file handling in Python.")
f.close()   # Closing the file

# Opening the same file in read mode
f = open("demo.txt", "r")
content = f.read()
print(content)
f.close()   # Closing the file