"""
Topic: Tuples, Dictionaries, and Looping in Python
Description: Demonstrates usage of immutable tuples, dictionary operations, and loops with conditionals.
"""

# -------------------------------
# Tuples: Immutable collections
# -------------------------------

# Tuple with different data types
Tuple = (1, 2, 'Hello', 5.5, 1)

# Tuple with nested lists (positive indexing)
Tuple = ([0], [1], [2], [3], [4])

# Print the type of Tuple
print(type(Tuple))

# Accessing tuple elements
print(Tuple[1])
print(Tuple[-1])
print(Tuple[-3])

# Uncommenting the below line would raise an error because tuples are immutable
# Tuple[0] = 10  # ❌ Not allowed

# Tuple methods
Tuple = (1, 2, 'Hello', 5.5, 1)
print(Tuple.count(2))      # Count of value 2
print(Tuple.index(5.5))    # Index of value 5.5

# -------------------------------
# Dictionaries: Key-value mapping
# -------------------------------

dict1 = {
    'name': 'Talal',
    'age': 18,
    'Occ': 'Std'
}

# Accessing values
value = dict1['age']
print(f'Age: {value}')
print(f"Age (again): {dict1['age']}")

# Adding new key-value pair
dict1['Occupation'] = 'Student'
print(dict1)

# Updating existing value
dict1['name'] = 'Ali'
print(dict1)

# Removing a key-value pair and saving its value
removed_value = dict1.pop('age')
print(dict1)
print(removed_value)

# Accessing keys, values, and items
print(f"Keys: {dict1.keys()}")
print(f"Values: {dict1.values()}")
print(f"Items: {dict1.items()}")

# Membership check
print(f"Does 'name' exist? {'name' in dict1}")
print(f"Does 'city' exist? {'city' in dict1}")

# Check for a specific key
if 'class' in dict1:
    print(f"Class is: {dict1['class']}")

# -------------------------------
# Loops with lists and conditions
# -------------------------------

# Searching an item in a list
List = ['apples', 'bananas', 'pears']
target_item = 'guavas'

for item in List:
    if item == target_item:
        print('Exist')
        break
else:
    print('Not Exist')

# Counting items greater than a certain value
numbers = [1, 5, 10, 15, 20, 25]
count_greater_than_10 = 0

for num in numbers:
    if num > 10:
        count_greater_than_10 += 1

print(count_greater_than_10)

# Using enumerate to access index and value
for index, item in enumerate(numbers):
    if index == 2:
        print(f"Item at index {index}: {item}")

# -------------------------------
# Looping through a dictionary
# -------------------------------

grades = {
    'Math': 90,
    'Eng': 76,
    'Sci': 85
}

for subject, grade in grades.items():
    if grade >= 85:
        print(f"Subject {subject} has a grade of {grade} (A)")
    else:
        print(f"Subject {subject} has a grade of {grade} (satisfactory)")
