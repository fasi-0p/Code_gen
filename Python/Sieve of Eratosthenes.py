def sieve(n):
    """
    Sieve of Eratosthenes:
    - Efficient way to find all primes ≤ n.
    - Marks all multiples of primes as non-prime.
    - Time Complexity: O(n log log n)
    """
    primes = [True] * (n + 1)  # Assume all numbers are prime
    primes[0], primes[1] = False, False  # 0 and 1 are not primes

    p = 2
    while p * p <= n:
        if primes[p]:
            # Mark all multiples of p as False
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    # Return list of all prime numbers
    return [i for i in range(n + 1) if primes[i]]

# ✅ Example
print("Primes ≤ 30:", sieve(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
