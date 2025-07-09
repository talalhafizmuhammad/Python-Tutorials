'''File Handling -> It allows us to write the data into non volatile memory
allows us to read and write from and to a file

-> read  (r)
-> write  (w)
-> append  (a)

method 1:
file = open('filename', 'mode')

file = open('file1.txt', 'r')  #error in read mode if file does not exist
method 1 to open and write in file
file = open('file1.txt', 'w')
file.write("This is my first line\n")
file.write('This is my second line')
file.close()


method 2

with open("file1.txt", 'w') as file:
    file.write("This is my first line\n")
    file.write('Welcome')
file.close() no need to use, automatically handles
    

READING from the file 
3 methods: .read(), .readline(), .readlines()
.read() -> read the contents as they are given
.readline() -> Just prints first line of content in the file
.readlines() -> prints the lines in the form of list elements

method 1 to read contents 
file = open("file1.txt", 'r')
a = file.readlines()
print(a)
file.close()

method 2

with open('file1.txt', 'r') as file:
    a = file.read()
    print(a)

append in a file -> writes the content to a file without deleting the existing one

method 1:
file = open("file.txt", 'a')
file.write("This is tutorial 8\n")
file.close()

method 2:
with open('file.txt', 'a') as file:
    file.write("Welcome to pythoneers ")

r+ -> Read and write
w+ -> write and read
a+ -> append and read

with open('file.txt', 'r+') as file:
    print(f"Content before updating: {file.read()}")
    file.write("\nAppended content")
    file.seek(70) #places the file pointer to the 70th position
    file.seek(0)  #places the file ptr to start
    print(f"Content after updating: {file.read()}")
'''
