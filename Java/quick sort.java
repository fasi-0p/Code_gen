import java.util.Arrays;

public class QuickSort {

    // QuickSort function (recursive)
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // Partition the array and get pivot index
            int pi = partition(arr, low, high);

            // Recursively sort elements before and after partition
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    // Partition function to place pivot in correct position
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];  // Take last element as pivot
        int i = low - 1;        // Index of smaller element

        // Traverse through all elements
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap pivot with element at i+1
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;  // Return pivot index
    }

    // ✅ Use-case
    public static void main(String[] args) {
        int[] nums = {10, 7, 8, 9, 1, 5};  // Unsorted array

        quickSort(nums, 0, nums.length - 1);  // Perform quicksort

        // Output sorted array
        System.out.println("Sorted: " + Arrays.toString(nums));  // [1, 5, 7, 8, 9, 10]
    }
}
