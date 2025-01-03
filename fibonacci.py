
def fibonacci_series(n):
    a, b = 0, 1

    # Print the Fibonacci series up to n terms
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update a and b for the next Fibonacci numbers

    print()  # Newline after printing the series

# Input the desired number of terms
n = int(input("Enter the number of terms: "))

# Call the fibonacci_series function with the input value
fibonacci_series(n)

