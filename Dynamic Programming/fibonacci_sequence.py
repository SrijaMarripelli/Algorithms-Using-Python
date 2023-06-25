def fibonacci_sequence(n):
    # Initialize the first two numbers of the sequence
    fib_sequence = [0, 1]

    # Generate the sequences uo to the nth term
    for i in range(2, n):
        # Calculate the next number in the sequence as the sum of the previous two numbers
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        # Add the next number to the sequence
        fib_sequence.append(next_number)

    # Return the Fibonacci sequence
    return fib_sequence        

fib_seq = fibonacci_sequence(10)
print(fib_seq)