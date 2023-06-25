def knapsack(capacity, weights, values, n):
    # Initialize matrix with zeros
    K = [[0 for x in range(capacity+1)] for x in range(n+1)]
    
    # Fill the matrix in bottom-up fashion
    for i in range(n+1):
        for w in range(capacity+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    
    # Find the maximum value that can be obtained
    max_value = K[n][capacity]
    
    # Find the items that were selected
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if max_value <= 0:
            break
        if max_value == K[i-1][w]:
            continue
        else:
            items.append(i-1)
            max_value -= values[i-1]
            w -= weights[i-1]
    
    # Reverse the items list so it is in the correct order
    items.reverse()
    
    # Return the maximum value and the items selected
    return max_value, items


# Example input
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
n = len(values)

# Call the function and print the output
max_value, items = knapsack(capacity, weights, values, n)
print("Maximum value:", max_value)
print("Items selected:", items)



"""
************************************
UNDER REVIEW
************************************
"""