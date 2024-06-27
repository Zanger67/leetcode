class Solution {
    public int[] distinctNumbers(int[] nums, int k) {
        int[] output = new int[nums.length - k + 1];
        HashMap<Integer, Integer> window = new HashMap<>();

        for (int i = 0; i < k - 1; i++) {
            window.put(nums[i], window.getOrDefault(nums[i], 0) + 1);
        }

        for (int i = k - 1; i < nums.length; i++) {
            window.put(nums[i], window.getOrDefault(nums[i], 0) + 1);

            output[i - k + 1] = window.size();

            if (window.get(nums[i - k + 1]) == 1) {
                window.remove(nums[i - k + 1]);
            } else {
                window.put(nums[i - k + 1], window.get(nums[i - k + 1]) - 1);
            }
        }

        return output;
    }
}