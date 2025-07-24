def factorial_recursive(n):
    """
    Factorial (Recursive):
    - n! = n * (n-1)!
    - Base case: 0! = 1
    - Time Complexity: O(n)
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """
    Factorial (Iterative):
    - Loop through 1 to n and multiply.
    - Time Complexity: O(n)
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# ✅ Example
print("Factorial Rec(5):", factorial_recursive(5))  # Output: 120
print("Factorial Iter(6):", factorial_iterative(6))  # Output: 720
