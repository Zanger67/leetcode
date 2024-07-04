class Solution {
    public int minOperations(int[] nums) {
        int turns = 0;

        int[] hasmap = new int[]{1, 0};
        boolean flipped = false;

        for (int i = 0; i < nums.length; i++) {
            int current = flipped ? hasmap[nums[i]] : nums[i];
            if (current == 0) {
                turns += 1;
                flipped = !flipped;
            }
        }

        if (!flipped
            && nums[nums.length - 1] == 1)
            return turns;

        else if (nums[nums.length - 1] == 0)
            return turns;

        return -1;   
    }
}