"""
Topic: Python Built-in Module - random
Covers:
- Generating random numbers
- Random selections
- Shuffling
- Dice simulation
"""

import random

# Generate a random floating-point number between 0.0 and 1.0
num = random.random()
print(f"Random float between 0 and 1: {num}")

# Generate a random integer between 1 and 10
num = random.randint(1, 10)  # Both start and end values are inclusive
print(f"Random integer between 1 and 10: {num}")

# Choose a random element from a list
fruits = ['apples', 'bananas', 'grapes']
rand_choice = random.choice(fruits)
print(f"Randomly selected fruit: {rand_choice}")

# Shuffle a list randomly
lst = [1, 2, 3, 4, 5]
print(f"Before shuffle: {lst}")
random.shuffle(lst)
print(f"After shuffle: {lst}")

# Simulate rolling two dice and print their sum
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(f"Die 1: {die1}, Die 2: {die2}")
print(f"Sum of two dice: {die1 + die2}")
