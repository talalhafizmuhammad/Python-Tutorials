'''tuples are immutable 
Tuple = (1, 2, 'Hello', 5.5, 1)
Tuple = ([0], [1], [2], [3], [4]....) positive
Tuple= (....[-5], [-4], [-3], [-2], [-1])

print(type(Tuple))

accessing elements
print(Tuple[1])
print(Tuple[-1])
print(Tuple[-3])

Tuple[0] = 10
print(Tuple)
print(Tuple.count(2))
print(Tuple.index(5.5))

dictionaries


dict1 = {'name' : 'Talal', 'age' : 18, 'Occ' : 'Std'}

value = dict1['age']
print(f'age: {value}')
print(f'Age: {dict1['age']}')

dict1['Occupation'] = 'Student'

print(dict1)

dict1['name'] = 'ali'
print(dict1)

dict2 = dict1.pop('age')
print(dict1)
print(dict2)

dict2 = dict1.keys()
print(f'Keys: {dict2}')


if 'class' in dict1:
    print(f"Name is: {dict1['name']}")

dict2 = dict1.values()
print(dict2)

dict2 = dict1.items()
print(dict2)

print(f"Does name exist? {'name' in dict1}")
print(f"Does city exist? {'city' in dict1}")

List = ['apples', 'bananas', 'pears']

target_item = 'guavas'

for i in List:
    if i == target_item:
        print('Exist')
    else:
        print('not')

numbers = [1, 5, 10, 15, 20, 25]

count_greater_than_10 = 0

for i in numbers:
    if i > 10:
        count_greater_than_10 += 1
print(count_greater_than_10)
for index, item in enumerate(numbers):
    if index == 2:
        print(f"item at index {index}: {item}")

dict1 = {'Math' : 90, 'Eng' : 76, 'Sci' : 85}

for subject, grade in dict1.items():
    if grade >= 85:
        print(f"Subject {subject} has grade of {grade} (A)")
    else:
        print(f"Subject {subject} has grade of {grade} (satisfactory)")

'''