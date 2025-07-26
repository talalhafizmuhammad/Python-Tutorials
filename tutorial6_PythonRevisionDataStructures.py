"""
Topic: Lists, Sets, Tuples, and Dictionaries with Loops in Python
Covers:
- Basics of each data structure
- Element access, manipulation
- Looping with for-loops
"""

# ---------------------------- Lists ----------------------------
# Mutable, ordered, allows mixed data types
myList = [0, True, 2, 'Hello', 4.5]
print(type(myList))

# Accessing elements
print(myList[1])     # Positive indexing
print(myList[-2])    # Negative indexing

# Adding elements
myList.append(6)
myList.insert(3, 'Bye')   # Insert at index 3
print(myList)

# Removing elements
myList.remove(True)       # Removes first occurrence
myList.pop()              # Removes last element
myList.pop(1)             # Removes element at index 1
print(myList)

# Length
print(f"Length of list is {len(myList)}")

# Membership test
print("Is 2 in list? ", 2 in myList)
print("Is 'bye' in list? ", 'bye' in myList)

# Loop through list
for i in myList:
    print(i, end=' ')

print("\n")

# ---------------------------- Sets ----------------------------
# Unordered, no duplicates
mySet = {1, 'Hello', 3, 4, 5.5, False}
print(mySet)

mySet.add(False)    # Duplicate; no effect
print(mySet)

# Removing elements
mySet.remove(3)
# mySet.remove(10)  # Would raise error if not in set
mySet.discard(10)   # Safe remove
print(mySet)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {1, 3}

print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference (set1 - set2): {set1.difference(set2)}")
print(f"Is set3 subset of set1? {set3.issubset(set1)}")
print(f"Is set3 superset of set1? {set3.issuperset(set1)}")

# Loop through set
for i in set1:
    print(i, end=' ')

print("\n")

# ---------------------------- Tuples ----------------------------
# Ordered, immutable
myTuple = (True, 2, 'hello', 4, 5.5)
print(type(myTuple))

# Access
print(myTuple[2])
print(myTuple[-3])

# Concatenation
tup1 = (1, 2, 3, 4)
tup2 = (True, False)
tup3 = tup1 + tup2 + myTuple
print(tup3)

# Length and membership
print(f"Length of tup1: {len(tup1)}")
print("Is 7 in tuple?", 7 in myTuple)

# Loop
for i in myTuple:
    print(i, end=' ')

print("\n")

# ---------------------------- Dictionaries ----------------------------
# Key-value pairs
myDict = {'name': 'Talal', 'age': 18, 'email': 'abc@gmail'}
print(myDict)

# Accessing values
print(f"Name: {myDict['name']}")
print(f"Age: {myDict.get('age')}")

# Add / Update
myDict['email'] = 'abc_updated@gmail'
myDict['age'] = 25
print(myDict)

# Remove
myDict.pop('age')
del myDict['name']
print(myDict)

# Keys, Values, Items
myDict = {'name': 'Talal', 'age': 18, 'email': 'abc@gmail'}
print(f"Keys: {myDict.keys()}")
print(f"Values: {myDict.values()}")
print(f"Items: {myDict.items()}")

# Looping
students = {'name': 'Ali', 'age': 20, 'grade': 'A-'}

# Using keys
for key in students:
    print(key, '->', students[key])

# Using items
for key, value in students.items():
    print(key, '=', value)

# Even numbers from list
myList = [1, 2, 3, 4, 5]
for i in myList:
    if i % 2 == 0:
        print(i)
