def binary_search(arr, key):
    i, j = 0, len(arr) - 1    
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            i = mid + 1
        else:
            j = mid - 1
    return -1
arr = [3,7,9,12,15,18,20]
key = int(input("Enter the element to search: "))
result = binary_search(arr, key)
if result != -1:
    print(f"Element found at index {result} in the sorted array")
else:
    print(f"Element not found in the array")
