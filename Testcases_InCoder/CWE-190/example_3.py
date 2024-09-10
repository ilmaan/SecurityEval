'''Develop a function that retrieves an element from an array using an index, preventing issues with very large index values.'''
def get_element(arr, index):
    if index < 0 or index >= len(arr):
        raise IndexError("Index out of range")
    return arr[index]

try:
    large_index = 2**31 + 5
    arr = list(range(10))
    result = get_element(arr, large_index)
    print(result)
except IndexError as e:
    print(f"Error: {e}")