data = {'1': ['a', 'b'], '2': ['c', 'd']}

combinations = []

for item1 in data['1']:
    for item2 in data['2']:
        combinations.append(item1 + item2)

print("All combinations of letters:")
print(combinations)