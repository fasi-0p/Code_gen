public class Factorial {

    // Iterative factorial
    public static long factorialIterative(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++)
            result *= i;
        return result;
    }

    // Recursive factorial
    public static long factorialRecursive(int n) {
        if (n == 0 || n == 1)
            return 1;  // Base case
        return n * factorialRecursive(n - 1);  // Recursive case
    }

    public static void main(String[] args) {
        int n = 5;

        long resultIter = factorialIterative(n);
        long resultRecur = factorialRecursive(n);

        System.out.println("Iterative factorial of " + n + " = " + resultIter);  // 120
        System.out.println("Recursive factorial of " + n + " = " + resultRecur);  // 120
    }
}
