my_list = input("Enter a list of words: ").split()

large_word = max(my_list, key=len)

length_of_large_word = len(large_word)

print("The longest word is:", large_word)
print("Its length is:", length_of_large_word)