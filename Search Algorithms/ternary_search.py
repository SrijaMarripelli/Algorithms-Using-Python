def ternary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        first_third = left + (right - left) // 3
        second_third = left + 2 * (right - left) // 3

        if arr[first_third] == target:
            return first_third
        elif arr[second_third] == target:
            return second_third
        elif arr[first_third] > target:
            right = first_third - 1
        elif arr[second_third] < target:
            left = second_third + 1
        else:
            left = first_third + 1
            right = second_third - 1
            
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = ternary_search(arr, target)
print(result)