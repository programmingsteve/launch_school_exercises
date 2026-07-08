# Write a function that returns a list that contains every other element of a
# list that is passed in as an argument. The values in the returned list should
# be those values that are in the 1st, 3rd, 5th, and so on elements of the
# argument list.

# Examples
# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

def oddities(items):
    result = []
    index = 0
    while index < len(items):
        result.append(items[index])
        index += 2

    return result

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

# Bonus question: Try to solve the problem using list slicing.

def bonus_oddities(items):
    return items[::2]

print(bonus_oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(bonus_oddities([1, 2, 3, 4]) == [1, 3])        # True
print(bonus_oddities(["abc", "def"]) == ['abc'])     # True
print(bonus_oddities([123]) == [123])                # True
print(bonus_oddities([]) == [])                      # True

# Write a companion function that returns the 2nd, 4th, 6th, and so on elements
# of a list.

# Try to solve this differently from the exercise described above.

def companion_oddities(items):
    result = []
    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])

    return result

print(companion_oddities([2, 3, 4, 5, 6]) == [3, 5])  # True
print(companion_oddities([1, 2, 3, 4]) == [2, 4])     # True
print(companion_oddities(["abc", "def"]) == ['def'])  # True
print(companion_oddities([123]) == [])                # True
print(companion_oddities([]) == [])                   # True
