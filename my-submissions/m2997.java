// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/

class Solution {
    public int minOperations(int[] nums, int k) {
        for (int num : nums) {
            k ^= num;
        }

        int counter = 0;
        while (k > 0) {
            if (k % 2 == 1) {
                counter++;
            }
            
            k = k >> 1;
        }

        return counter;
    }
}