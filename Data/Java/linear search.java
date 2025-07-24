public class LinearSearch {

    // Function to perform linear search
    public static int linearSearch(int[] nums, int target) {
        // Iterate through each element
        for (int i = 0; i < nums.length; i++) {
            // Check if current element matches the target
            if (nums[i] == target)
                return i;  // Return index if found
        }
        // Target not found in array
        return -1;
    }

    // ✅ Use-case
    public static void main(String[] args) {
        int[] nums = {5, 3, 8, 6, 2};  // Unsorted array
        int target = 6;

        int index = linearSearch(nums, target);

        // Output result
        System.out.println("Index of " + target + ": " + index);  // Output: 3
    }
}
