def merge_sort(arr):
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves into the original array
        i = j = k =0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half or right_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Usage of the algorithm
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Sorted array is: ", arr)