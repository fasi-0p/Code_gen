public class LCM {

    // Helper function to compute GCD (reused)
    public static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    // Function to compute LCM using formula: (a * b) / gcd(a, b)
    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }

    public static void main(String[] args) {
        int a = 15, b = 20;

        int result = lcm(a, b);

        System.out.println("LCM of " + a + " and " + b + " is: " + result);  // Output: 60
    }
}
