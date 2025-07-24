def quick_sort(arr):
    """
    Quick Sort Algorithm:
    - Picks a pivot element, partitions array into two halves:
      one with elements less than pivot, one with greater.
    - Recursively sorts the sub-arrays.
    - Time Complexity: O(n log n) average, O(n^2) worst case
    """
    if len(arr) <= 1:
        return arr  # Base case: array is already sorted

    pivot = arr[0]  # Pick first element as pivot

    # Partition the array into left and right of pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    # Recursively sort left and right, and combine with pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

# ✅ Example
nums = [10, 7, 8, 9, 1, 5]
nums = quick_sort(nums)
print("Quick Sorted:", nums)  # Output: [1, 5, 7, 8, 9, 10]
