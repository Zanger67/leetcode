class Solution {
    public int removeElement(int[] nums, int val) {
        int pointer = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[pointer] = nums[i];
                pointer += 1;
            }
        }
        return pointer;
    }
}