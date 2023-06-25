def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = linear_search(arr, target)
print(result)