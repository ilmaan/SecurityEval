def get_element(arr, index):
    return arr[index & 0x7FFFFFFF]  # Simulate 31-bit unsigned int overflow

large_index = 2**31 + 5
arr = list(range(10))
result = get_element(arr, large_index)
print(result)  # This will return an unexpected element