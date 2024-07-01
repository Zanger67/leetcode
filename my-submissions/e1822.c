int arraySign(int* nums, int numsSize) {
    bool out = true;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < 0)
            out = !out;
        if (!nums[i])
            return 0;
    }
    return out ? 1 : -1;
}