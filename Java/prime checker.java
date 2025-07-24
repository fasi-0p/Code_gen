public class PrimeChecker {

    // Function to check if a number is prime
    public static boolean isPrime(int n) {
        if (n <= 1) return false;  // Not prime
        if (n == 2) return true;   // 2 is prime

        // Check for divisibility from 2 to sqrt(n)
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0)
                return false;  // Divisible => not prime
        }

        return true;  // No divisors => prime
    }

    public static void main(String[] args) {
        int n = 29;

        boolean result = isPrime(n);

        System.out.println(n + " is prime? " + result);  // Output: true
    }
}
