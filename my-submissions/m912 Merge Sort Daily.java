class Solution {
    public int[] sortArray(int[] nums) {
        return mergeSort(nums);
    }

    private int[] mergeSort(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        }

        int[] left = mergeSort(Arrays.copyOfRange(nums, 0, nums.length / 2));
        int[] right = mergeSort(Arrays.copyOfRange(nums, nums.length / 2, nums.length));

        int leftIndx = 0, rightIndx = 0;
        int i = 0;
        while (leftIndx < left.length && rightIndx < right.length) {
            if (left[leftIndx] < right[rightIndx]) {
                nums[i] = left[leftIndx];
                ++leftIndx;
            } else {
                nums[i] = right[rightIndx];
                ++rightIndx;
            }
            ++i;
        }

        while (leftIndx < left.length) {
            nums[i] = left[leftIndx];
            ++leftIndx;
            ++i;
        }
        while (rightIndx < right.length) {
            nums[i] = right[rightIndx];
            ++rightIndx;
            ++i;
        }
        return nums;
    }
}