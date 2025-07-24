#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& nums, int left, int mid, int right) {
    vector<int> temp;
    int i = left, j = mid + 1;

    // Merge both halves into temp[]
    while (i <= mid && j <= right) {
        if (nums[i] <= nums[j])
            temp.push_back(nums[i++]);
        else
            temp.push_back(nums[j++]);
    }

    // Copy remaining elements
    while (i <= mid) temp.push_back(nums[i++]);
    while (j <= right) temp.push_back(nums[j++]);

    // Copy back to original array
    for (int k = 0; k < temp.size(); k++)
        nums[left + k] = temp[k];
}

void mergeSort(vector<int>& nums, int left, int right) {
    if (left >= right) return;

    int mid = left + (right - left) / 2;
    mergeSort(nums, left, mid);        // Sort left half
    mergeSort(nums, mid + 1, right);   // Sort right half
    merge(nums, left, mid, right);     // Merge halves
}

// ✅ Use-case
int main() {
    vector<int> nums = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(nums, 0, nums.size() - 1);
    for (int x : nums)
        cout << x << " ";  // Output: 3 9 10 27 38 43 82
}
