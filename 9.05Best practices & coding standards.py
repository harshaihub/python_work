#📝 Best Practices
#Write modular code  
#Break functionality into small functions (e.g., add_task(), mark_done(), organize_files()).

#Use meaningful names  
#Variables, functions, and classes should clearly describe their purpose (tasks, get_file_type, Calculator).

#Error handling  
#Always anticipate edge cases (division by zero, empty task list, missing folder).

#Keep code DRY (Don’t Repeat Yourself)  
#Avoid duplicating logic; reuse functions wherever possible.

#Documentation & comments  
#Add  docstrings ("""This function adds a task""") and inline comments for clarity.

#Version control  
#Use Git to track changes and collaborate effectively.

#📐 Coding Standards (Python)
#PEP 8 style guide

#Indentation: 4 spaces.

#Line length: ≤ 79 characters.

#Blank lines: Separate functions/classes with 2 blank lines.

#Imports: Group standard library, third‑party, and local imports separately.

#Naming conventions

#Variables/functions: snake_case → add_task, file_type.

#Classes: PascalCase → TaskManager.

#Constants: UPPER_CASE → MAX_TASKS.

#Consistent formatting  
#Use tools like black or autopep8 to auto‑format code.

#🔍 Testing Standards
#Unit tests for each function  
#Example: Test add() separately from divide() in Calculator.

#Test edge cases

#Division by zero.

#Empty task list.

#Unknown file type.

#Use setUp() and tearDown() in unittest  
#Reset state before/after each test to avoid interference.

#Automate testing  
#Run tests with:

#bash
#python -m unittest discover
#This finds all test files automatically.

#🚀 Professional Touch
#Logging: Use Python’s logging module instead of print statements for debugging.

#Configuration files: Store settings (like folder paths) in a config file.

#Scalability: Design with future expansion in mind (e.g., To‑Do List could later support deadlines or priorities).