// https://leetcode.com/problems/daily-temperatures/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int* output = (int*) malloc(sizeof(int) * temperaturesSize);
    *returnSize = temperaturesSize;
    int currentMaxTemp = 0;

    for (int i = temperaturesSize - 1; i >= 0; i--) {
        if (temperatures[i] >= currentMaxTemp) {
            currentMaxTemp = temperatures[i];
            output[i] = 0;
            continue;
        }

        int offset = 1;
        while (temperatures[i] >= temperatures[i + offset]) {
            offset += output[i + offset];
        }

        output[i] = offset;
    }

    return output;
}