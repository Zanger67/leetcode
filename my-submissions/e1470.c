/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int* output = (int*) malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;

    for (int i = 0; i < n; i++) {
        output[2 * i] = nums[i];
        output[2 * i + 1] = nums[i + n];
    }

    return output;
}