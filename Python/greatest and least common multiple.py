def gcd(a, b):
    """
    GCD (Greatest Common Divisor):
    - Finds the largest number that divides both a and b.
    - Uses Euclidean Algorithm.
    - Time Complexity: O(log(min(a, b)))
    """
    while b != 0:
        a, b = b, a % b  # Replace a with b, and b with a % b
    return a

def lcm(a, b):
    """
    LCM (Least Common Multiple):
    - Finds smallest number divisible by both a and b.
    - lcm(a, b) = abs(a*b) // gcd(a, b)
    """
    return abs(a * b) // gcd(a, b)

# ✅ Example
print("GCD(48, 18):", gcd(48, 18))    # Output: 6
print("LCM(4, 5):", lcm(4, 5))        # Output: 20
