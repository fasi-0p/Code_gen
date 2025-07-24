import java.util.*;

public class StackExample {

    public static void main(String[] args) {
        // Create a Stack of Integers
        Stack<Integer> stack = new Stack<>();

        // Push elements onto stack
        stack.push(10);  // Push 10
        stack.push(20);  // Push 20
        stack.push(30);  // Push 30

        System.out.println("Stack after pushing: " + stack);  // [10, 20, 30]

        // Pop elements from stack
        int top = stack.pop();  // Pops 30 (Last in, first out)
        System.out.println("Popped: " + top);  // 30
        System.out.println("Stack now: " + stack);  // [10, 20]
    }
}
