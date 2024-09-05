import os

def read_file(filename):
    filepath = os.path.join("data_directory", filename)
    if not os.access(filepath, os.R_OK):
        raise PermissionError("You don't have permission to read this file")
    with open(filepath, 'r') as file:
        return file.read()

try:
    print(read_file("sensitive_data.txt"))
except PermissionError as e:
    print(f"Error: {e}")