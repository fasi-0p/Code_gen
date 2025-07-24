#include <iostream>
using namespace std;

bool isPowerOfTwo(int n) {
    // A power of 2 has only one set bit (e.g., 1000, 0100)
    return n > 0 && (n & (n - 1)) == 0;
}

// ✅ Use-case
int main() {
    int n = 16;
    cout << n << " is power of 2? " << (isPowerOfTwo(n) ? "Yes" : "No") << endl;  // Output: Yes
}
