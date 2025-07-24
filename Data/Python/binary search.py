def binary_search(arr, target):
    """
    Performs binary search on a list to find the target element.
    The array is sorted before performing the search.
    Returns the index of target in the sorted array if found, else -1.
    """
    # First, sort the array to ensure binary search works correctly
    arr.sort()  # This is an in-place sort (Timsort, O(n log n))

    # Set the initial left and right pointers for binary search
    left = 0
    right = len(arr) - 1

    # Continue the loop while the search space is valid
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2

        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid
        # If target is less than mid element, search left half
        elif arr[mid] > target:
            right = mid - 1
        # If target is greater than mid element, search right half
        else:
            left = mid + 1

    # If target not found in array
    return -1


# 🔍 Use-case Example
# Suppose we have an unsorted list of employee IDs
employee_ids = [1100, 1001, 1150, 1078, 1054, 1023, 1012]
search_id = 1078

# Call the binary search function
result = binary_search(employee_ids, search_id)

# Output the result
if result != -1:
    print(f"Employee ID {search_id} found at index {result} in the sorted array.")
else:
    print(f"Employee ID {search_id} not found in the database.")
