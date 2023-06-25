def radix_sort(arr):
    # Determine the maximum number of digits in the input array
    max_digit = len(str(max(arr)))

    # Iterate over each digit, starting from the least significant
    for digit in range(max_digit):
        # Create buckets for each possible value of the current digit
        buckets = [[] for _ in range(10)]

        # Place each element in the input array into the appropriate bucket
        for element in arr:
            digit_value = (element // (10**digit)) % 10
            buckets[digit_value].append(element)

        # Concatenate the buckets in order to form a sorted version of the array
        arr = [element for bucket in buckets for element in bucket]

    return arr

# Example usage
arr = [170, 45,75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(sorted_arr)