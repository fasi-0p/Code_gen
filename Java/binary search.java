public class BinarySearch {

    // Returns index if found, else -1
    public static int binarySearch(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;  // Prevent overflow

            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                left = mid + 1;  // Search right
            else
                right = mid - 1; // Search left
        }

        return -1;  // Not found
    }

    public static void main(String[] args) {
        int[] nums = {2, 4, 6, 8, 10, 12};  // Must be sorted
        int target = 8;
        int index = binarySearch(nums, target);

        System.out.println("Index of " + target + ": " + index);  // Output: 3
    }
}
