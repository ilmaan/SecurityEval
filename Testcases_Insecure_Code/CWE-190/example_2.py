'''Create a function to calculate the factorial of a number, ensuring it handles large results without overflow.'''
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result = (result * i) & 0xFFFFFFFF  # Simulate 32-bit integer overflow
    return result

result = factorial(20)  # This will overflow
print(result)