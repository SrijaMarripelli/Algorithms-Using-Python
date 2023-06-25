def heap_sort(arr):
    n = len(arr)

    # Build a max heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap pne by one and place them in their final position
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    # Find the largest element among the root node and its two children 
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[left_child] > arr[largest]:
       largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If the largest element is not the root node, swap the root node and the largest element and recursivelyheapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print("Sorted array is: ", arr)