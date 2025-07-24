#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& nums) {
    int n = nums.size();
    // Perform n-1 passes
    for (int i = 0; i < n - 1; i++) {
        // Push largest element to end in each pass
        for (int j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1])
                swap(nums[j], nums[j + 1]);  // Swap if in wrong order
        }
    }
}

// ✅ Use-case
int main() {
    vector<int> nums = {5, 1, 4, 2, 8};
    bubbleSort(nums);
    for (int num : nums)
        cout << num << " ";  // Output: 1 2 4 5 8
}
