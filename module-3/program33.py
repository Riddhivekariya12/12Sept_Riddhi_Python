dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'c': 40, 'd': 50}

combined_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

print("Combined dictionary with added values for common keys:", combined_dict)
