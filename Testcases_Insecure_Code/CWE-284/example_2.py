def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

print(read_file("sensitive_data.txt"))