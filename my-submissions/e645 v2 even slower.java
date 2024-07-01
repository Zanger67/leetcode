// Consistently 5% percentile --> bad runtime but works

class Solution {
    public int[] findErrorNums(int[] nums) {
        byte[] corrects = new byte[nums.length];

        int dupe = -1;
        for (int i = 0; i < nums.length; i++) {
            corrects[nums[i] - 1] += 1;

            if (corrects[nums[i] - 1] == 2) {
                dupe = nums[i];
            }
        }

        for (int i = 0; i < corrects.length; i++) {
            System.out.println(corrects[i]);
        }

        int index = 0;
        while (true) {
            if (corrects[index] == 0) {
                return new int[]{dupe, index + 1};
            }
            index++;
        }

    }
}