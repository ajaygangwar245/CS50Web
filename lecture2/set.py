# create a set
numbers = set()

# add some elements to the set
numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(4)

# print
print(numbers)

# add duplicate element
numbers.add(2)

# print
print(numbers)

# remove element
numbers.remove(2)

# print
print(numbers)

# total number of elements in the set
print(f"The set has {len(numbers)} elements.")