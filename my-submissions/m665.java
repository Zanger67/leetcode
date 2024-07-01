class Solution {
    public boolean checkPossibility(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (!(nums[i - 1] > nums[i])) {
                continue;
            }

            if (i + 1 >= nums.length) {
                return true;
            }

            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j - 1] > nums[j]) {
                    return false;
                }
            }

            if (i == 1) {
                return true;
            }

            return (nums[i - 2] <= nums[i]) || (nums[i - 1] <= nums[i + 1]);
        }

        return true;
    }
}