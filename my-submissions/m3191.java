class Solution {
    public int minOperations(int[] nums) {
        int turns = 0;

        int[] hasmap = new int[]{1, 0};

        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] == 0) {
                turns += 1;
                nums[i] = hasmap[nums[i]];
                nums[i + 1] = hasmap[nums[i + 1]];
                nums[i + 2] = hasmap[nums[i + 2]];
            }
        }

        if (nums[nums.length - 1] == 1 
            && nums[nums.length - 2] == 1
            && nums[nums.length - 3] == 1)
            return turns;
        return -1;   
    }
}