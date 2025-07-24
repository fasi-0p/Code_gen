import java.util.*;

public class HashMapExample {

    public static void main(String[] args) {
        // Create a HashMap to store String keys and Integer values
        HashMap<String, Integer> map = new HashMap<>();

        // Put key-value pairs
        map.put("apple", 2);
        map.put("banana", 5);
        map.put("orange", 3);

        System.out.println("HashMap: " + map);  // {banana=5, orange=3, apple=2}

        // Get value using key
        int count = map.get("banana");  // 5
        System.out.println("Bananas: " + count);

        // Check if a key exists
        if (map.containsKey("apple")) {
            System.out.println("We have apples.");  // true
        }
    }
}
