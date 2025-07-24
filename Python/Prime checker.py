def is_prime(n):
    """
    Prime Checker:
    - A prime number has exactly 2 divisors: 1 and itself.
    - Check for divisibility up to sqrt(n).
    - Time Complexity: O(√n)
    """
    if n <= 1:
        return False  # 0 and 1 are not prime
    if n <= 3:
        return True   # 2 and 3 are prime

    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate even numbers and multiples of 3

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Check divisibility by i and i+2
        i += 6
    return True

# ✅ Example
print("Is 29 Prime?:", is_prime(29))  # Output: True
print("Is 40 Prime?:", is_prime(40))  # Output: False
