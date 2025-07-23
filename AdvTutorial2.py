'''RANDOM module -> For Random numbers or Random Selections

import random

Generate a random floating point number:

num = random.random()
print(num)

Generating a random integer between 1 to 10:

num = random.randint(1, 10) #positional arguments are compulsory randint(starting_value, ending_value)
print(num)

choose a random element from a list
fruits = ['apples', 'bananas', 'grapes']
randchoice = random.choice(fruits)
print(randchoice)

Shuffling the list randomly:

lst = [1, 2, 3, 4, 5]
print(f"Before: {lst}")
random.shuffle(lst)
print(f"After: {lst}")

Simulate rolling two dice and print their sum

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(f"Sum is: {die1 + die2}")
'''