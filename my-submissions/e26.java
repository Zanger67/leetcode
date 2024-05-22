// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution {
    public int removeDuplicates(int[] nums) {
        int counter = 1;
        int shift = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                shift++;
            } else {
                counter++;
            }

            nums[i - shift] = nums[i];
        }

        return counter;
    }
}