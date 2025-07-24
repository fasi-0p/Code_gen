#include <iostream>
#include <vector>
using namespace std;

// Binary Search assumes array is sorted
int binarySearch(const vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;  // Prevent overflow

        if (nums[mid] == target)
            return mid;  // Target found
        else if (nums[mid] < target)
            left = mid + 1;  // Search right half
        else
            right = mid - 1; // Search left half
    }
    return -1;  // Not found
}

// ✅ Use-case
int main() {
    vector<int> nums = {1, 3, 5, 7, 9};
    int target = 5;

    int result = binarySearch(nums, target);
    cout << "Index of 5: " << result << endl;  // Output: 2
}
