#include <iostream>
using namespace std;

// Recursive method
long long factorialRec(int n) {
    if (n <= 1) return 1;        // Base case
    return n * factorialRec(n - 1);
}

// Iterative method
long long factorialIter(int n) {
    long long result = 1;
    for (int i = 2; i <= n; i++)
        result *= i;
    return result;
}

// ✅ Use-case
int main() {
    int n = 5;
    cout << "Recursive factorial of " << n << ": " << factorialRec(n) << endl;  // Output: 120
    cout << "Iterative factorial of " << n << ": " << factorialIter(n) << endl;  // Output: 120
}
