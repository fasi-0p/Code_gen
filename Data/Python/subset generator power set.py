def generate_subsets(nums):
    """
    Generate all subsets (power set):
    - Either include or exclude current element.
    - Backtracking used to explore all choices.
    - Time Complexity: O(2^n)
    """
    result = []

    def backtrack(index, path):
        if index == len(nums):
            result.append(path[:])  # Add a copy of current subset
            return
        # Exclude current
        backtrack(index + 1, path)
        # Include current
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()  # Backtrack

    backtrack(0, [])
    return result

# ✅ Example
print("Subsets:", generate_subsets([1, 2, 3]))
# Output: All subsets of [1, 2, 3]
