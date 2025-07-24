def merge_sort(arr):
    """
    Merge Sort Algorithm:
    - Divide and conquer approach.
    - Recursively splits the array into halves,
      then merges sorted halves.
    - Time Complexity: O(n log n)
    """
    if len(arr) > 1:
        # Find middle index
        mid = len(arr) // 2

        # Divide array into two halves
        L = arr[:mid]
        R = arr[mid:]

        # Recursively sort each half
        merge_sort(L)
        merge_sort(R)

        # Pointers for L, R, and main array
        i = j = k = 0

        # Merge elements back into arr
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy any remaining elements of L[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy any remaining elements of R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# ✅ Example
nums = [38, 27, 43, 3, 9]
merge_sort(nums)
print("Merge Sorted:", nums)  # Output: [3, 9, 27, 38, 43]
