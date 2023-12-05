main_list = [1, 2, 3, 4, 5, 6, 7, 8]
sub_list = [3, 4, 5]

contains_sublist = any(sub_list == main_list[i:i + len(sub_list)] for i in range(len(main_list) - len(sub_list) + 1))

print("Does the list contain the sublist?", contains_sublist)