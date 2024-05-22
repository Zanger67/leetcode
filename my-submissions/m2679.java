// https://leetcode.com/problems/sum-in-a-matrix/description/

class Solution {
    public int matrixSum(int[][] nums) {
        int sum = 0;

        for (int i = 0; i < Math.max(nums[0].length, nums.length); i++) {
            int[] temp = new int[nums.length];
            // PriorityQueue<Integer> pq = new PriorityQueue<>(nums.length, null);
            for (int j = 0; j < nums.length; j++) {
                int maxIndex = 0;
                for (int k = 0; k < nums[0].length; k++) {
                    if (nums[j][k] > nums[j][maxIndex]) {
                        maxIndex = k;
                    }
                }
                // pq.add(nums[j][maxIndex]);
                temp[j] = nums[j][maxIndex];
                nums[j][maxIndex] = 0;
            }

            // sum += pq.poll();

            int max = 0;
            for (int j = 0; j < temp.length; j++) {
                max = Math.max(max, temp[j]);
            }
            sum += max;
        }

        return sum;
    }   
}