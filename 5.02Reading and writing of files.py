#📘 Writing to a File
#Use open() with "w" (write) or "a" (append) mode.


# Writing to a file
f = open("demo.txt", "w")   # open in write mode
f.write("Hello Harshvardhan!\n")
f.write("Learning file handling in Python.")
f.close()   # close file

#📘 Reading from a File
#Use open() with "r" (read) mode.

# Reading entire file
f = open("demo.txt", "r")
content = f.read()   # reads whole file
print(content)
f.close()

#📘 Reading Line by Line
with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())
#👉 Reads each line separately until EOF.

#📘 Writing & Reading Together
#Use r+ (read/write) or a+ (append/read).

with open("demo.txt", "a+") as f:
    f.write("\nAdding another line.")
    f.seek(0)   # move pointer to start
    print(f.read())