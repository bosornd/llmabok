# tuple - immutable sequence
apple = ('apple', 100)
print(apple[1])  # Output: 100
apple[1] = 200   # TypeError: 'tuple' object does not support item assignment

apple = 'apple', [1, 2, 3]      # tupe without parentheses
print(apple[1])  # Output: [1, 2, 3]
apple[1].append(4)
print(apple)     # Output: ('apple', [1, 2, 3, 4])
