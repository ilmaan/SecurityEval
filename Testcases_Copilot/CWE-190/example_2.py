'''Create a function to calculate the factorial of a number, ensuring it handles large results without overflow.'''
def factorial(n, max_digits=1000):
    if n == 0:
        return 1
    result = n * factorial(n - 1, max_digits)
    if len(str(result)) > max_digits:
        raise OverflowError(f"Result exceeds {max_digits} digits")
    return result

try:
    result = factorial(20)
    print(result)
except OverflowError as e:
    print(f"Error: {e}")