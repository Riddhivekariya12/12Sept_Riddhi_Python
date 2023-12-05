list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

unzipped_lists = list(zip(*list_of_tuples))

print("Unzipped lists:", unzipped_lists)