#include <iostream>
#include <vector>
using namespace std;

void sieve(int n) {
    vector<bool> isPrime(n + 1, true);  // Initialize all as prime
    isPrime[0] = isPrime[1] = false;

    // Start eliminating multiples from 2
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i)
                isPrime[j] = false;     // Mark multiples as not prime
        }
    }

    // Print all prime numbers
    for (int i = 2; i <= n; i++)
        if (isPrime[i]) cout << i << " ";
}

// ✅ Use-case
int main() {
    int limit = 30;
    cout << "Primes up to " << limit << ": ";
    sieve(limit);  // Output: 2 3 5 7 11 13 17 19 23 29
}
