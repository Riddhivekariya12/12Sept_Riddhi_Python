main_string =input("enter a string:")
insert = input("enter a middle string:")

middle = len(main_string) // 2
new_string = main_string [:middle] + insert + main_string [middle:]

print(new_string)