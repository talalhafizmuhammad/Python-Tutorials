'''Modules: Contains built in python codes, which we import and use in other python codes
included by import keyword
-> function
-> classes
-> Variables

TYPES OF MODULES

-> Built in modules
-> User defined Modules
-> External modules

BUILT IN MODULES
1. OS Module

import os  #Helps to interact with the Operating System, enables the tasks with the directories or files 


To get current working directory
cwd = os.getcwd()
print(cwd)  #.getcwd()->getcurrentworkingdirectory

List the files in cwd
lstdir = os.listdir()
print(lstdir)

Create the new Directory
newDir = os.path.join(cwd, 'MyDir')
if not os.path.exists(newDir):
    os.mkdir(newDir)
    print(newDir)
else:
    print(f"Directory already exists")

Check if a file exists

Path = os.path.join(cwd, "Tutorial1.py")
if os.path.exists(Path):
    print(f"file exists")
else:
    print(f"file donot exists")

CMD Commands
print("jernfernfjkernfjnfejkrnerjknekjvne")
os.system('cls')

files = os.listdir(cwd)
for f in files:
    if f.endswith('.cpp'):
        print(f"{f} is a C++ file")

os.remove("C:/Users/User/Downloads/Rolls.pdf")
    '''