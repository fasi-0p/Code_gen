#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;      // 0 and 1 are not prime
    if (n == 2) return true;       // 2 is prime
    if (n % 2 == 0) return false;  // Eliminate even numbers

    // Only check till sqrt(n)
    for (int i = 3; i * i <= n; i += 2)
        if (n % i == 0) return false;

    return true;
}

// ✅ Use-case
int main() {
    int n = 29;
    cout << n << " is prime? " << (isPrime(n) ? "Yes" : "No") << endl;  // Output: Yes
}
