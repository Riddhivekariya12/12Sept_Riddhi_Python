my_dict = {'a': 4, 'b': 2, 'c': 7, 'd': 1}

ascending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))


descending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", ascending_sorted)
print("Descending order:", descending_sorted)