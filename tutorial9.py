'''r+ -> Read and write
w+ -> write and read
a+ -> append and read

with open('file.txt', 'r+') as file:
    print(f"Content before updating: {file.read()}")
    file.write("\nAppended content")
    file.seek(70) #places the file pointer to the 70th position
    file.seek(0)  #places the file ptr to start
    print(f"Content after updating: {file.read()}")


w+ mode
with open('file2.txt', 'w+') as file:
    file.write("First Line.\n")
    file.write('Second Line.\n')
    file.seek(0)
    content = file.read()
    print(f"After updating: {content}")

a+ mode

with open('file3.txt', 'a+') as file:
    file.write("This is my first line\n")
    file.write('This is my second line\n')
    file.seek(0, 0)
    contents = file.read()
    print(f"Contents updated are: {contents}")
    
seek(), and tell()

seek(offset, whence)
offset: Number of bytes to move
whence: Statring position (0: beginning, 1: current position, 2: end) default: 0

with open('file3.txt', 'a+') as file:
    # file.write("This is my first line\n")
    # file.write('This is my second line\n')
    file.seek(7, 0)
    contents = file.read()
    print(f"Contents updated are: {contents}")

tell() -> tells the position of pointer

with open('file3.txt', 'a+') as file:
    file.write("This is my first line\n")
    file.write('This is my second line\n')
    a = file.tell()
    contents = file.read()
    print(f"Contents updated are: {contents}")
    print(a)

with open("data.txt", 'r') as file:
    print(f"Initial Position: {file.tell()}")
    print(f"Reading content: {file.read()}")
    print(f"Final Position: {file.tell()}")
    file.seek(0)
    print(f"Position after seek(0): {file.tell()}")
    print(f"Reading content: {file.read()}")
    file.seek(20, 0)  #read 20 characters from the beginning
    print(f"Position after seek(20, 0): {file.tell()}")
    print(f"Reading content: {file.read()}")
    file.seek(0, 2)
    print(f"Position after seek(0, 2): {file.tell()}")
    print(f"Reading content: {file.read()}")
    print(file.closed) #check whether file is close or not
    print(f"File name: {file.name}, file mode: {file.mode}") #print name and mode of file
    
print(file.closed)

file.closed -> check if a file is close or not
file.name -> getting a file name
file.mode -> getting the file mode
'''
