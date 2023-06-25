def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Create a list to hold the counts of each element
    count_list = [0] * (max_element + 1)

    # Count the occurences of each element in the array
    for element in arr:
        count_list[element] += 1

    # Update the counts to be cumulative
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i-1]

    # Create a sorted list
    sorted_list = [0] * len(arr)
    for element in arr:
        sorted_list[count_list[element]-1] = element
        count_list[element] -= 1
    
    return sorted_list

# Example usage
arr = [5, 3, 2, 7, 4, 6, 1, 9, 8, 5]
sorted_arr = counting_sort(arr)
print(sorted_arr)