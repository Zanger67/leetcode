// https://leetcode.com/problems/maximum-total-reward-using-operations-i/description/
// https://leetcode.com/contest/weekly-contest-401/


// Tried doing this *after* the contest thinking huh if I spent an hour
// trying to do this quesiton in python and kept getting TLEs, what if I just
// wrote a brute forcey thing in C. Did it in 10 minutes right after the contest
// and it immediately passed. Sigh.

int compareHelper(const void* one, const void* two) {
    return *((int *) one) - *((int *) two);
}

int maxTotalReward(int* rewardValues, int rewardValuesSize) {
    int maxVall = 0;
    for (int i = 0; i < rewardValuesSize; i++) {
        if (maxVall < rewardValues[i]) 
            maxVall = rewardValues[i];
    }

    bool helper[2000 * 2 + 1] = {false};

    qsort(rewardValues, rewardValuesSize, sizeof(int), compareHelper);

    helper[0] = true;
    for (int i = 0; i < rewardValuesSize; i++) {
        for (int j = rewardValues[i] - 1; j >= 0; j--) {
            if (helper[j]) {
                helper[j + rewardValues[i]] = true;
            }
        }
    }

    for (int i = 2000 * 2; i >= 0; i--) {
        if (helper[i]) 
            return i;
    }

    return -1;
}