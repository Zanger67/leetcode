int maximumXOR(int* nums, int numsSize) {
    int output = 0;
    for (int i = 0; i < numsSize; i++) {
        output |= nums[i];
    }
    return output;
}