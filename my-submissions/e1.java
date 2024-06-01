// https://leetcode.com/problems/two-sum/


class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums.length == 2) {
            return new int[]{0, 1};
        }

        HashMap<Integer, Integer> ref = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (ref.containsKey(nums[i])) {
                return new int[]{ref.get(nums[i]), i};
            }

            ref.put((target - nums[i]), i);
        }

        // No solution (shouldn't occur given parameters provided)
        return new int[]{0, 0};
    }
}