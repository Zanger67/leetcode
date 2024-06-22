class Solution {
    public int minimumOperations(int[] nums) {
        int turns = 0;
        for (int num : nums) {
            if (num % 3 != 0) {
                turns += 1;
            }
        }

        return turns;
    }
}
