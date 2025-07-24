#include <iostream>
#include <vector>
using namespace std;

void permute(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }

    for (int i = start; i < nums.size(); i++) {
        swap(nums[start], nums[i]);  // Fix element at start
        permute(nums, start + 1, result);  // Recurse
        swap(nums[start], nums[i]);  // Backtrack
    }
}

// ✅ Use-case
int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result;

    permute(nums, 0, result);

    for (auto& p : result) {
        for (int x : p) cout << x << " ";
        cout << endl;
    }
}
