'''lists, sets, tuples and dictionaries with loops

List -> Mutuable, diff data types, sequenced
myList = [0, True, 2, 'Hello', 4.5]

print(type(myList))

Accessing elements

print(myList[1]) #+ve indexing
print(myList[-2])  #-ve indexing

ADDING ELEMENTS

myList.append(6)
print(myList)

myList.insert(3, 'Bye')  #.insert(index, value)
print(myList)


REMOVING ELEMENTS

myList.remove(True)
print(myList)

myList.pop()
print(myList)

myList.pop(1)
print(myList)

length of list

print(f"Length of list is {len(myList)}")

Element exist or not

print("Is 2 in list? ", 2 in myList)
print("is 'bye' in list? ", 'bye' in myList)

for i in myList:
    print(i, end = ' ')

SETS -> Unordered form, do not allow duplicates

mySet = {1, 'Hello', 3, 4, 5.5, False}

print((mySet))

mySet.add(False)
print((mySet))

remove

mySet.remove(3)
print(mySet)

mySet.remove(10)
print(mySet)

mySet.discard(10)
print(mySet)

union, intersection, difference, issubset, issuperset

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {1, 3}

print(f"Union is {set1.union(set2)}")
print(f"Intersection is {set1.intersection(set2)}")
print(f"Difference is {set1.difference(set2)}")  #set1 - set2
print(f"Check that is it subset? {set3.issubset(set1)}")
print(f"Check that is superset? {set3.issuperset(set1)}")

for i in set1:
    print(i, end = ' ')

Tuples -> Ordered, immutable

myTuple = (True, 2, 'hello', 4, 5.5)

print(type(myTuple))

Access

print(myTuple[2])
print(myTuple[-3])

myTuple[1] = 10  error
myTuple.append(6)
myTuple.remove(2)

Concatenation
tup1 = (1, 2, 3, 4)
tup2 = (True, False)
tup3 = tup1 + tup2 + myTuple
print(tup3)

print(f"Length is {len(tup1)}")

print("Is 7 in tuple?", 7 in myTuple)

for i in myTuple:
    print(i, end = ' ')

Dictionaries -> key value pairs

myDict = {'name' : 'Talal', 'age' : 18, 'email' : 'abc@gmail'}
print(myDict)

Accessing values
var = myDict['name']
print(f"Name is {var}")

var = myDict.get('age')
print(f"Age is {var}")
add
myDict['email'] = 'abc@gmail'
print(myDict)
update
myDict['age'] = 25
print(myDict)

remove
myDict.pop('age')
print(myDict)

del
del myDict['name']
print(myDict)

myDict = {'name' : 'Talal', 'age' : 18, 'email' : 'abc@gmail'}

print(f"Keys are: {myDict.keys()}")
print(f"Values are: {myDict.values()}")

print(f"Items are: {myDict.items()}")

students = {
    'name': 'Ali',
    'age': 20,
    'grade': 'A-'
}

Loop through keys

for i in students:
    print(i, '->', students[i])

.items()

for i, j in students.items():
    print(i, '=', j)

myList = [1, 2, 3, 4, 5]

for i in myList:
    if i % 2 == 0:
        print(i)
        '''