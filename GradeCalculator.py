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
