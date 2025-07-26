"""
Topic: Python Modules (Advanced)
Covers:
- Built-in Modules
- OS Module Usage
- File and Directory Handling
- Executing System Commands
"""

import os  # Helps interact with the operating system (files, directories, commands)

# Current Working Directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# List files in current directory
files = os.listdir()
print(f"Files in Directory:\n{files}")

# Create a new directory if it doesn't exist
new_dir = os.path.join(cwd, 'MyDir')
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"New directory created: {new_dir}")
else:
    print("Directory 'MyDir' already exists.")

# Check if a specific file exists
file_path = os.path.join(cwd, "main.cpp")
if os.path.exists(file_path):
    print("main.cpp exists in the directory.")
else:
    print("main.cpp does not exist.")

# List all Python files in current directory
print("\nPython files in current directory:")
for f in files:
    if f.endswith('.py'):
        print(f"{f}")

# List all C++ files in current directory
print("\nC++ files in current directory:")
for f in files:
    if f.endswith('.cpp'):
        print(f"{f}")

# Clear screen (Windows command; for Linux/Mac use 'clear')
os.system('cls')
print("Screen cleared using os.system('cls')")

# Deleting a file (use with caution)
# Uncomment to use
# os.remove("C:/Users/User/Desktop/PythonAdvance/main.cpp")

# Attempting to remove a directory using os.remove will raise an error
# os.remove("C:/Users/User/Desktop/PythonAdvance/folder")  # Error: cannot remove directory
