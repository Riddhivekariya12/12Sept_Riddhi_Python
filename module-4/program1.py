file_path = 'your_file_path.txt'  # Replace 'your_file_path.txt' with the path to your text file

with open(file_path, 'r') as file:
    content = file.read()
    print(content)