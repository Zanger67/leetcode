// https://leetcode.com/problems/concatenation-of-array/description/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int* output = (int*) malloc(sizeof(int) * 2 * numsSize);
    *returnSize = 2 * numsSize;

    for (int i = 0; i < numsSize; i++) {
        output[i] = nums[i];
        output[i + numsSize] = nums[i];
    }

    return output;
}