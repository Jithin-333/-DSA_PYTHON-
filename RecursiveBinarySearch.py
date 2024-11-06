def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)  
arr = [1, 3, 5, 7, 9, 11, 13, 15]

# Recursive version
index = binary_search_recursive(arr, 7, 0, len(arr) - 1)
if index != -1:
    print(f"Value found at index: {index}")
else:
    print("Value not found")
