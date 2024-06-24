class Solution {
    public int maximumXOR(int[] nums) {
        int output = 0;
        for (int num : nums) {
            output |= num;
        }

        return output;
    }
}