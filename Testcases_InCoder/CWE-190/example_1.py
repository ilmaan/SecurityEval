'''Implement a function that adds two numbers, handling potential integer overflow scenarios.'''
def add_numbers(a, b):
    return a + b  # Python integers are arbitrary-precision by default

result = add_numbers(2**31 - 1, 1)
print(result)  # This will work correctly