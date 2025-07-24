import java.util.*;

public class QueueExample {

    public static void main(String[] args) {
        // Create a Queue using LinkedList
        Queue<Integer> queue = new LinkedList<>();

        // Enqueue elements
        queue.add(1);  // Add 1
        queue.add(2);  // Add 2
        queue.add(3);  // Add 3

        System.out.println("Queue after adding: " + queue);  // [1, 2, 3]

        // Dequeue element
        int removed = queue.remove();  // Removes 1 (First in, first out)
        System.out.println("Removed: " + removed);  // 1
        System.out.println("Queue now: " + queue);  // [2, 3]
    }
}
