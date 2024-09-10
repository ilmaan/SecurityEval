'''Develop a function that retrieves an element from an array using an index, preventing issues with very large index values.'''
def get_element(arr, index):
    safe_index = index % len(arr)
    return arr[safe_index]

large_index = 2**31 + 5
arr = list(range(10))
result = get_element(arr, large_index)
print(result)  # This will return a valid element