bool divideArray(int* nums, int numsSize) {
    bool vals[501] = {false};

    for (int i = 0; i < numsSize; i++) {
        vals[nums[i]] = !vals[nums[i]];
    }

    for (int i = 1; i <= 500; i++) {
        if (vals[i]) {
            return false;
        }
    }
    return true;
}