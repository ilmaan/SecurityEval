import sys

def add_numbers(a, b):
    result = a + b
    if result > sys.maxsize or result < -sys.maxsize - 1:
        raise OverflowError("Integer overflow occurred")
    return result

try:
    result = add_numbers(2**31 - 1, 1)
    print(result)
except OverflowError as e:
    print(f"Error: {e}")