keys_list = ['a', 'b', 'c']
values_list = [1, 2, 3]

mapped_dict = {key: value for key, value in zip(keys_list, values_list)}

print("Mapped dictionary:", mapped_dict)
