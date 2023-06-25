def insertion_sort(arr):
    # traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
            print(arr)
        arr[j+1] = key
        # print("iteration-"+str(i)+": "+str(arr))

# example usage
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array is: ", arr)