'''while condition:
    associated code
print(1)
print(2)
...
print(10)
a = 1 
while a <= 10:
    print(a)
    a += 1

print("Hello", end = '')
print(" World")
    
break
continue
a = 0
while a < 10:
    print(a)
    if a == 5:
        continue
    a += 1
    
for loop

for condition:
    code
a = 0
for i in range(1, 11):
    print(i)

data structures

list, tuples, dictionaries and sets

List = [1, 2, True, 5.5, 'Hello']   #mutuable, different data types storage
print(len(List))
List = [[0], [1], [2], [3], [4]]  #forward(positive)
List = [[-5], [-4], [-3], [-2], [-1]] #negative
print(type(List))
print(List[4])
print(List[-1])
print(List[-5])

adding elements

List.append(29)  #add elements to the last
print(List)

insert elements
List.insert(2, 29)
print(List)
print(len(List))

List.insert(3, 'World')
print(List)
print(len(List))
List = [1, 2, True, 5.5, 'Hello']   #mutuable, different data types storage

List.remove('Hello')
print(List)
pop function 
popped = List.pop(0)
print(f'popped item: {popped}')
print(List)
modify 
List[0] = 10
List[2] = False
print(List)

Sets
Set = {1,2,3,4,4}
print(Set)
print(len(Set))

taking union
Set1 = {1, 2, 'Hello', 4}
Set2 = {3, 4, 5, 6}
UnionOfSet = Set2.union(Set1)
print(UnionOfSet)
taking intersection
Intersection = Set1.intersection(Set2)
print(f'Intersection = {Intersection}')

Difference (A-B)
Diff = Set2 - Set1
print(f'Difference = {Diff}')

Set1.add(1)
print(Set1)
Set1.remove('Hello')
print(Set1)
# Set1.clear()
print(Set1)
a = (input())
if a is True:
    print('Hy')
    '''