# list
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)        # Output: ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits[1])     # Output: 'apple'

print(fruits[0])     # Output: orange
print(fruits[1:3])   # Output: ['apple', 'pear']
print(fruits[-1])    # Output: banana
print(fruits[-3:-1]) # Output: ['kiwi', 'apple']
print(fruits.index('banana')) # Output: 3
print(fruits.count('banana')) # Output: 2

del fruits[1:4]
print(fruits)        # Output: ['orange', 'kiwi', 'apple', 'banana']

fruits.sort()
for fruit in fruits:
    print(fruit, end=' ')  # Output: apple banana kiwi orange 

squares = [x**2 for x in range(10)]
print(squares)       # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

points = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(points)        # Output: [(1, 3), (1, 4), (2, 3), (2, 4), (3, 1), (3, 4)]

# set
fruits = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}
print(fruits)        # Output: {'pear', 'kiwi', 'banana', 'apple', 'orange'}
# print(fruits[1])   # TypeError: 'set' object is not subscriptable

# tuple - immutable sequence
apple = ('apple', 100)
print(apple)         # Output: ('apple', 100)
print(apple[1])      # Output: 100
# apple[1] = 200     # TypeError: 'tuple' object does not support item assignment

apple = 'apple', [1, 2, 3]      # tuple without parentheses
print(apple[1])      # Output: [1, 2, 3]
apple[1].append(4)
print(apple)         # Output: ('apple', [1, 2, 3, 4])

# dictionary
costs = {'apple': 100, 'banana': 200, 'kiwi': 300}
print('kiwi' in costs)         # Output: True
print(costs['kiwi'])           # Output: 300
print(costs.get('orange', 0))  # Output: 0

for fruit, cost in costs.items():
    print(f"{fruit}: {cost}")  # Output: apple: 100, banana: 200, kiwi: 300