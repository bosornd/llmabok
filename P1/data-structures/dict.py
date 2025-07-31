# dictionary of costs
costs = {'apple': 100, 'banana': 200, 'kiwi': 300}

print('kiwi' in costs)         # Output: True
print(costs['kiwi'])           # Output: 300
print(costs.get('orange', 0))  # Output: 0

for fruit, cost in costs.items():
    print(f"{fruit}: {cost}")  # Output: apple: 100, banana: 200, kiwi: 300
