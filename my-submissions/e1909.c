bool canBeIncreasing(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) { // val to ignore
        bool increasing = true;
        int j = 0;
        for (j; j < numsSize - 1; j++) {
            if (j == i) {
                continue;
            }
            int compare = j + 1;
            if (compare == i) {
                compare++;
            }
            if (compare >= numsSize) {
                continue;
            }

            if (nums[j] >= nums[compare]) {
                increasing = false;
                break;
            }
        }

        if (increasing) {
            return true;
        }
    }
    return false;
}