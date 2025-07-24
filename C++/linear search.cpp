#include <iostream>
#include <vector>
using namespace std;

// Linear search checks every element
int linearSearch(const vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == target)
            return i;  // Found at index i
    }
    return -1;  // Not found
}

// ✅ Use-case
int main() {
    vector<int> nums = {4, 2, 9, 1, 6};
    int result = linearSearch(nums, 1);
    cout << "Index of 1: " << result << endl;  // Output: 3
}
