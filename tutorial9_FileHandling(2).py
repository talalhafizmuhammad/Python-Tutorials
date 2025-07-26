"""
Topic: File Handling - Part 2
Covers:
- r+, w+, a+ modes
- seek() and tell() functions
- Metadata access: file.name, file.mode, file.closed
"""

# r+ mode: Read and write (must exist)
with open('file.txt', 'r+') as file:
    print("Content before updating:")
    print(file.read())
    file.write("\nAppended content")
    file.seek(0)
    print("Content after updating:")
    print(file.read())

# w+ mode: Write and read (creates or overwrites)
with open('file2.txt', 'w+') as file:
    file.write("First Line.\n")
    file.write("Second Line.\n")
    file.seek(0)
    content = file.read()
    print("After updating (w+):")
    print(content)

# a+ mode: Append and read (creates if not exists)
with open('file3.txt', 'a+') as file:
    file.write("This is my first line\n")
    file.write("This is my second line\n")
    file.seek(0)
    contents = file.read()
    print("Contents updated (a+):")
    print(contents)

# seek(offset, whence)
# offset: Number of bytes to move
# whence: 0 = beginning, 1 = current, 2 = end

with open('file3.txt', 'a+') as file:
    file.seek(7, 0)  # Move 7 bytes from the start
    contents = file.read()
    print("Reading from byte 7:")
    print(contents)

# tell() - tells current pointer position
with open('file3.txt', 'a+') as file:
    file.write("Appending one more line\n")
    position = file.tell()
    file.seek(0)
    contents = file.read()
    print("Contents with new append:")
    print(contents)
    print(f"Current file pointer is at: {position}")

# Demonstrating seek and tell in detail
with open("data.txt", 'r') as file:
    print(f"Initial Position: {file.tell()}")
    print(f"Reading content: {file.read()}")
    print(f"Final Position: {file.tell()}")
    
    file.seek(0)
    print(f"After seek(0), position: {file.tell()}")
    print("Reading content again:")
    print(file.read())

    file.seek(20, 0)
    print(f"After seek(20, 0), position: {file.tell()}")
    print(file.read())

    file.seek(0, 2)
    print(f"After seek(0, 2), position (EOF): {file.tell()}")
    print("Trying to read at EOF:")
    print(file.read())

    # File metadata
    print(f"File closed? {file.closed}")
    print(f"File name: {file.name}")
    print(f"File mode: {file.mode}")

# Outside the context manager, file is closed
print(f"File closed outside block? {file.closed}")
