import java.util.*;

public class Permutations {

    static void permute(int[] nums, List<Integer> current, boolean[] used, List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;

            used[i] = true;                       // Mark as used
            current.add(nums[i]);                // Choose
            permute(nums, current, used, result); // Explore
            current.remove(current.size() - 1);  // Unchoose
            used[i] = false;                      // Unmark
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        List<List<Integer>> result = new ArrayList<>();
        permute(nums, new ArrayList<>(), new boolean[nums.length], result);

        for (List<Integer> p : result)
            System.out.println(p);
    }
}
