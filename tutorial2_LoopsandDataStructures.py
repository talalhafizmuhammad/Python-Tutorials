"""
Topic: While Loops, For Loops, and Basic Data Structures in Python
Description: Demonstrates usage of loops (while, for), lists, and sets with example operations.
"""

# While Loop Example: Print numbers from 1 to 10
a = 1
while a <= 10:
    print(a)
    a += 1

# Output without newline using 'end'
print("Hello", end='')
print(" World")

# Demonstrating 'break' and 'continue' (with continue example)
a = 0
while a < 10:
    print(a)
    if a == 5:
        a += 1  # Fix: increment before continue to avoid infinite loop
        continue
    a += 1

# For Loop Example: Print 1 to 10
for i in range(1, 11):
    print(i)

# -----------------------------
# Data Structures: Lists
# -----------------------------

# A list with multiple data types (mutable)
List = [1, 2, True, 5.5, 'Hello']
print(len(List))

# Nested list examples with positive and negative indexing
List = [[0], [1], [2], [3], [4]]
print(type(List))
print(List[4])    # Access by positive index
print(List[-1])   # Access by negative index
print(List[-5])

# Adding elements to a list
List.append(29)  # Add to end
print(List)

# Inserting elements at a specific position
List.insert(2, 29)
print(List)
print(len(List))

List.insert(3, 'World')
print(List)
print(len(List))

# Removing an element by value
List = [1, 2, True, 5.5, 'Hello']
List.remove('Hello')
print(List)

# Removing an element by index using pop
popped = List.pop(0)
print(f'Popped item: {popped}')
print(List)

# Modifying elements in a list
List[0] = 10
List[2] = False
print(List)

# -----------------------------
# Data Structures: Sets
# -----------------------------

# Set automatically removes duplicates
Set = {1, 2, 3, 4, 4}
print(Set)
print(len(Set))

# Union of two sets
Set1 = {1, 2, 'Hello', 4}
Set2 = {3, 4, 5, 6}
UnionOfSet = Set2.union(Set1)
print(UnionOfSet)

# Intersection of two sets
Intersection = Set1.intersection(Set2)
print(f'Intersection = {Intersection}')

# Difference (A - B)
Diff = Set2 - Set1
print(f'Difference = {Diff}')

# Adding and removing elements from sets
Set1.add(1)
print(Set1)

Set1.remove('Hello')
print(Set1)

# Clear (commented out to retain data for demo)
# Set1.clear()
print(Set1)

# Note: 'is' checks for identity, not value equality
a = input()
if a == 'True':  # Use == instead of 'is' for string comparison
    print('Hy')
