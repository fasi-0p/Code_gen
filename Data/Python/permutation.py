def generate_permutations(nums):
    """
    Generate all permutations of nums:
    - Fix each element at index, swap, and recurse.
    - Time Complexity: O(n!)
    """
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])  # Store a copy
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)  # Fix next element
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo)

    backtrack(0)
    return result

# ✅ Example
print("Permutations:", generate_permutations([1, 2, 3]))
