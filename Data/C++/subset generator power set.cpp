#include <iostream>
#include <vector>
using namespace std;

void generateSubsets(int i, vector<int>& nums, vector<int>& current, vector<vector<int>>& result) {
    if (i == nums.size()) {
        result.push_back(current);  // Reached end, store current subset
        return;
    }

    // Include nums[i]
    current.push_back(nums[i]);
    generateSubsets(i + 1, nums, current, result);

    // Exclude nums[i]
    current.pop_back();
    generateSubsets(i + 1, nums, current, result);
}

// ✅ Use-case
int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result, current;

    generateSubsets(0, nums, current, result);

    for (auto& subset : result) {
        cout << "[ ";
        for (int x : subset) cout << x << " ";
        cout << "]\n";
    }
}
