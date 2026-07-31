#📘 Why Exception Handling in File Operations?
 #Files may not exist (error: FileNotFoundError).
#You may not have permission (error: PermissionError).
#File operations may fail due to I/O errors.

#Exception handling ensures the program runs smoothly even if errors occur.

#🧩 Example: Safe File Reading

try:
    f = open("demo.txt", "r")
    content = f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("Unexpected error:", e)

#👉 This prevents the program from crashing if demo.txt doesn’t exist.

#🧩 Example: Writing with with + Exception Handling

try:
    with open("demo.txt", "w") as f:
        f.write("Hello Harshvardhan!\n")
        f.write("Exception handling makes file operations safe.")
except Exception as e:
    print("Error while writing:", e)

#👉 Using with ensures the file closes automatically, even if an error occurs.