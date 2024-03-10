def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def print_fibonacci_series(n):
    fib_sequence = fibonacci(n)
    print("Fibonacci Series:")
    for num in fib_sequence:
        print(num)

# Example usage
n = 10
print_fibonacci_series(n)







