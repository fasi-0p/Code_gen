#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> mp;

    // Insert key-value pairs
    mp["apple"] = 5;
    mp["banana"] = 2;

    // Access value
    cout << "apple count: " << mp["apple"] << endl;  // Output: 5

    // Check if key exists
    if (mp.find("banana") != mp.end())
        cout << "banana exists\n";

    // Iterate hashmap
    for (auto& pair : mp)
        cout << pair.first << ": " << pair.second << endl;
}
