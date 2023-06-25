def quick_sort(arr, low, high):
    if low < high :
        # Partition the array and get the index of the pivot element
        pivot_index = partition(arr, low, high)

        # Recursively sort the two sub-arrays
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]

    # Initialize the pivot index as the leftmost element
    pivot_index = low

    # Iterate through the array and move all elements less than or equal to the pivot to the left of the pivot index
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1

    # Move the pivot to its final position
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Return the pivot index
    return pivot_index

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array is: ", arr)