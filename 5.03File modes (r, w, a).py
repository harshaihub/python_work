#| Mode     | Meaning           | Behavior      |
#| ``"r"`` | Read | Opens file for reading. File must exist. |
#| ``"w"`` | Write | Opens file for writing. Creates new file if not exists, overwrites if exists. |
#| ``"a"`` | Append | Opens file for writing. Creates new file if not exists, adds content at end without overwriting. |

#1. Read Mode ("r")

f = open("demo.txt", "r")
print(f.read())   # Reads entire file
f.close()
#👉 Requires file to exist, otherwise error.

#2. Write Mode ("w")

f = open("demo.txt", "w")
f.write("Hello Harshvardhan!\n")
f.write("This will overwrite old content.")
f.close()
#👉 If file exists, old content is erased.

#3. Append Mode ("a")

f = open("demo.txt", "a")
f.write("\nThis line is appended.")
f.close()
#👉 Adds new content at the end, keeps old content intact.
