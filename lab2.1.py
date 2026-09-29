def linear_search_sorted(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
        elif arr[i]> key:
            return -1
    return -1

arr = [1,4,6,8,9,12,15,16,19]
key = int(input("enter the element to be found:"))
result=linear_search_sorted(arr,key)

if result==-1:
    print("element not found")
else:
    print(f"element found at index : {result} ")
