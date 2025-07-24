public class GCD {

    // Function to find GCD using recursion (Euclidean algorithm)
    public static int gcd(int a, int b) {
        // Base case: if b becomes 0, a is the GCD
        if (b == 0)
            return a;

        // Recursive call: gcd(b, a % b)
        return gcd(b, a % b);
    }

    public static void main(String[] args) {
        int a = 36, b = 60;

        int result = gcd(a, b);

        // Output result
        System.out.println("GCD of " + a + " and " + b + " is: " + result);  // Output: 12
    }
}
