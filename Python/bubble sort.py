def bubble_sort(arr):
    """
    Bubble Sort Algorithm:
    - Repeatedly steps through the list, compares adjacent elements,
      and swaps them if they're in the wrong order.
    - Time Complexity: O(n^2)
    """
    n = len(arr)

    # Traverse the array n times
    for i in range(n):
        # Inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # If current element is greater than next, swap
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# ✅ Example
nums = [64, 34, 25, 12, 22]
bubble_sort(nums)
print("Bubble Sorted:", nums)  # Output: [12, 22, 25, 34, 64]
