list_of_tuples = [(1, 2), (), (3, 4), (), (), (5, 6, 7), ()]

filtered_tuples = [tup for tup in list_of_tuples if tup]

print("Filtered list after removing empty tuples:", filtered_tuples)