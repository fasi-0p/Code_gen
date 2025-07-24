import java.util.Arrays;

public class MergeSort {

    // Main mergeSort function (recursive)
    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            // Find the mid index
            int mid = left + (right - left) / 2;

            // Sort the left half
            mergeSort(arr, left, mid);

            // Sort the right half
            mergeSort(arr, mid + 1, right);

            // Merge the sorted halves
            merge(arr, left, mid, right);
        }
    }

    // Merge function to combine two sorted subarrays
    private static void merge(int[] arr, int l, int m, int r) {
        // Calculate sizes of the two subarrays
        int n1 = m - l + 1;
        int n2 = r - m;

        // Create temp arrays
        int[] left = new int[n1];
        int[] right = new int[n2];

        // Copy data into temp arrays
        for (int i = 0; i < n1; i++)
            left[i] = arr[l + i];
        for (int j = 0; j < n2; j++)
            right[j] = arr[m + 1 + j];

        // Initial indices of subarrays
        int i = 0, j = 0, k = l;

        // Merge the two arrays back into arr[]
        while (i < n1 && j < n2) {
            if (left[i] <= right[j])
                arr[k++] = left[i++];
            else
                arr[k++] = right[j++];
        }

        // Copy remaining elements of left[], if any
        while (i < n1)
            arr[k++] = left[i++];

        // Copy remaining elements of right[], if any
        while (j < n2)
            arr[k++] = right[j++];
    }

    // ✅ Use-case
    public static void main(String[] args) {
        int[] nums = {5, 3, 8, 4, 2};  // Unsorted array

        mergeSort(nums, 0, nums.length - 1);  // Sort the array

        // Output sorted array
        System.out.println("Sorted: " + Arrays.toString(nums));  // [2, 3, 4, 5, 8]
    }
}
