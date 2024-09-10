'''Implement a function that adds two numbers, handling potential integer overflow scenarios.'''
def add_numbers(a, b):
    return a + b

# Simulating 32-bit integer overflow
result = add_numbers(2**31 - 1, 1) & 0xFFFFFFFF
print(result)  # This will overflow