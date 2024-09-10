'''Create a function to calculate the factorial of a number, ensuring it handles large results without overflow.'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(20)  # This will work correctly
print(result)