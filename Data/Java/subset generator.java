import java.util.*;

public class Subsets {

    static void generateSubsets(int[] nums, int index, List<Integer> current, List<List<Integer>> result) {
        // Add current subset to result
        result.add(new ArrayList<>(current));

        for (int i = index; i < nums.length; i++) {
            current.add(nums[i]);  // Choose
            generateSubsets(nums, i + 1, current, result);  // Explore
            current.remove(current.size() - 1);  // Un-choose
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        List<List<Integer>> result = new ArrayList<>();
        generateSubsets(nums, 0, new ArrayList<>(), result);

        for (List<Integer> subset : result)
            System.out.println(subset);
    }
}
