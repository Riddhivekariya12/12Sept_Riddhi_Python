strings_list = ["aba", "xyz", "aa", "abc", "1221"]

count = 0
for string in strings_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print(f"Number of strings meeting the conditions: {count}")