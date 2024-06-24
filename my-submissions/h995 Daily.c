int minKBitFlips(int* nums, int numsSize, int k) {
    int flips = 0;
    int windowFlips = 0;
    int hmap[] = {1, 0};

    bool flipped[numsSize];
    memset(flipped, 0, sizeof(bool) * numsSize);

    for (int i = 0; i < numsSize; i++) {
        if (i >= k && flipped[i - k]) {
            windowFlips--;
        }

        int current = nums[i];

        if (windowFlips % 2) {
            current = hmap[current];
        }

        if (!current) {
            if (i + k > numsSize) {
                return -1;
            }

            windowFlips++;
            flips++;
            flipped[i] = true;
        }
    }
    return flips;
}