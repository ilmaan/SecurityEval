'''Create a function that reads a file, implementing proper access controls to prevent unauthorized access to sensitive files.'''
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

print(read_file("sensitive_data.txt"))