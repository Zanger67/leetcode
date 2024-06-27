int triangularSum(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < numsSize - i - 1; j++) {
            nums[j] = (nums[j] + nums[j + 1]) % 10;
        }
    }

    return nums[0] % 10;
}