#include <iostream>
using namespace std;

// Recursive function to compute GCD
int gcd(int a, int b) {
    if (b == 0) return a;          // Base case: if b is 0, return a
    return gcd(b, a % b);          // Recur with b and remainder
}

// LCM using GCD formula: lcm(a,b) = (a*b) / gcd(a,b)
int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;    // Avoid overflow by dividing first
}

// ✅ Use-case
int main() {
    int a = 12, b = 18;
    cout << "GCD: " << gcd(a, b) << endl;   // Output: 6
    cout << "LCM: " << lcm(a, b) << endl;   // Output: 36
}
