"""
Topic: File Handling in Python
Covers:
- Opening files in different modes
- Writing to files
- Reading from files
- Appending to files
- Using with-context manager
- File pointer control with seek()
"""

# File Handling allows us to read/write data into non-volatile memory

# Modes:
# 'r'  -> read mode
# 'w'  -> write mode (overwrites)
# 'a'  -> append mode
# 'r+' -> read + write
# 'w+' -> write + read
# 'a+' -> append + read

# Method 1: Writing to a file using open()
file = open('file1.txt', 'w')
file.write("This is my first line\n")
file.write("This is my second line")
file.close()

# Method 2: Writing to a file using 'with' (auto-handles closing)
with open("file1.txt", 'w') as file:
    file.write("This is my first line\n")
    file.write("Welcome")

# Reading from a file
# .read() reads full content
# .readline() reads only the first line
# .readlines() returns a list of all lines

# Method 1: Reading contents
file = open("file1.txt", 'r')
lines = file.readlines()
print(lines)
file.close()

# Method 2: Reading with context manager
with open('file1.txt', 'r') as file:
    content = file.read()
    print(content)

# Appending to an existing file (doesn't delete previous data)

# Method 1
file = open("file1.txt", 'a')
file.write("\nThis is tutorial 8\n")
file.close()

# Method 2
with open('file1.txt', 'a') as file:
    file.write("Welcome to pythoneers")

# Reading + Writing using r+, w+, a+
with open('file1.txt', 'r+') as file:
    print("Content before updating:")
    print(file.read())

    file.write("\nAppended content")

    file.seek(0)  # Reset pointer to beginning
    print("Content after updating:")
    print(file.read())
