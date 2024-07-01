/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    int* output = (int*) malloc(sizeof(int) * numsSize);
    int outputCurrent = 0;
    *returnSize = numsSize;

    int neg = 0;
    int pos = 0;
    while (outputCurrent < numsSize) {
        while (nums[neg] > 0) {
            neg++;
        }
        while (nums[pos] < 0) {
            pos++;
        }

        output[outputCurrent] = nums[pos];
        output[outputCurrent + 1] = nums[neg];
        outputCurrent += 2;
        neg++;
        pos++;
    }

    return output;
}