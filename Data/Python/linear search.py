def linear_search(arr, target):
    """
    Linear Search Algorithm:
    - Iterates through every element to find the target.
    - Works on unsorted arrays.
    - Time Complexity: O(n)
    """
    # Traverse each index in the array
    for i in range(len(arr)):
        # Check if current element is the target
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Not found

# ✅ Example
nums = [10, 2, 8, 4]
print("Linear Search Result:", linear_search(nums, 8))  # Output: 2
