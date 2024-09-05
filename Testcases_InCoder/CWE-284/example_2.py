import os

ALLOWED_FILES = {"public_data.txt", "user_info.txt"}

def read_file(filename):
    if filename not in ALLOWED_FILES:
        raise PermissionError("Access to this file is not allowed")
    filepath = os.path.join("safe_directory", filename)
    with open(filepath, 'r') as file:
        return file.read()

try:
    print(read_file("sensitive_data.txt"))
except PermissionError as e:
    print(f"Error: {e}")