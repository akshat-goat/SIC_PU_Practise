def fibonacci_memoized(n, memo={}):

    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
        memo[n] = result
        return result

if __name__ == "__main__":
    print("--- Fibonacci Sequence Generator (Memoized) ---")
    num_index = int(input("Enter the index (N) for the Fibonacci number: "))
    if num_index < 0:
        print("Index must be non-negative.")
    else:
        fib_num = fibonacci_memoized(num_index)
        print(f"The {num_index}th Fibonacci number is: {fib_num}")
