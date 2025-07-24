def is_power_of_two(n):
    """
    Power of Two:
    - A number is power of 2 if there's only one bit set in binary.
    - n & (n-1) == 0 → only one bit was set.
    - Time Complexity: O(1)
    """
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# ✅ Example
print("Is 16 power of 2?:", is_power_of_two(16))  # Output: True
print("Is 18 power of 2?:", is_power_of_two(18))  # Output: False
