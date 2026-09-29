def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # use the returned sorted list
    right = merge_sort(arr[mid:])  # use the returned sorted list
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")
for _ in range(n):
    arr.append(int(input()))

sorted_arr = merge_sort(arr)
print("Sorted array:", *sorted_arr)
