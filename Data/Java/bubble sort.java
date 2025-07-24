import java.util.Arrays;

public class BubbleSort {

    // Function to perform bubble sort
    public static void bubbleSort(int[] nums) {
        int n = nums.length;

        // Perform n-1 passes
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;  // Track if any swaps occurred in this pass

            // Compare adjacent elements
            for (int j = 0; j < n - i - 1; j++) {
                // If left is greater than right, swap them
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                    swapped = true;  // Mark that we swapped
                }
            }

            // If no swaps, the array is already sorted
            if (!swapped) break;
        }
    }

    // ✅ Use-case
    public static void main(String[] args) {
        int[] nums = {5, 2, 9, 1, 5, 6};  // Unsorted array

        bubbleSort(nums);  // Sort array using bubble sort

        // Output sorted array
        System.out.println("Sorted: " + Arrays.toString(nums));  // [1, 2, 5, 5, 6, 9]
    }
}
