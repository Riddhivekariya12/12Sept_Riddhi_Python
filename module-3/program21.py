list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10

modified_tuples = []

for tup in list_of_tuples:
    modified_list = list(tup)
    modified_list[-1] = new_value
    modified_tuples.append(tuple(modified_list))

print(modified_tuples)