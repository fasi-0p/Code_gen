import java.util.Arrays;

public class Sieve {

    // Function to print all primes <= n
    public static void sieve(int n) {
        // Initialize boolean array to true
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);  // Assume all numbers are prime

        isPrime[0] = false;
        isPrime[1] = false;

        // Eliminate non-primes
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                // Mark all multiples of i as non-prime
                for (int j = i * i; j <= n; j += i)
                    isPrime[j] = false;
            }
        }

        // Print remaining primes
        System.out.print("Primes <= " + n + ": ");
        for (int i = 2; i <= n; i++) {
            if (isPrime[i])
                System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int n = 50;
        sieve(n);
        // Output: Primes <= 50: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
    }
}
