public class PowerOfTwo {

    // Function to check if n is power of 2
    public static boolean isPowerOfTwo(int n) {
        // A number is power of two if it has only one set bit in binary
        return n > 0 && (n & (n - 1)) == 0;
    }

    public static void main(String[] args) {
        int n = 16;

        boolean result = isPowerOfTwo(n);

        System.out.println(n + " is power of two? " + result);  // Output: true
    }
}
