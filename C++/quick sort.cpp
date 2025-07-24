#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& nums, int low, int high) {
    int pivot = nums[high];  // Choose last element as pivot
    int i = low - 1;         // Index for smaller element

    for (int j = low; j < high; j++) {
        if (nums[j] < pivot) {
            i++;
            swap(nums[i], nums[j]);  // Move smaller element to left
        }
    }
    swap(nums[i + 1], nums[high]);  // Place pivot in correct position
    return i + 1;
}

void quickSort(vector<int>& nums, int low, int high) {
    if (low < high) {
        int pi = partition(nums, low, high);  // Partition index
        quickSort(nums, low, pi - 1);         // Sort left part
        quickSort(nums, pi + 1, high);        // Sort right part
    }
}

// ✅ Use-case
int main() {
    vector<int> nums = {10, 7, 8, 9, 1, 5};
    quickSort(nums, 0, nums.size() - 1);
    for (int x : nums)
        cout << x << " ";  // Output: 1 5 7 8 9 10
}
