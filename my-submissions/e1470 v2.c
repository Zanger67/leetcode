// I presume this is much faster cause there's no multiplication anymore

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int* output = (int*) malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    
    int pt1 = 0;
    int pt2 = n;
    for (int i = 0; i < numsSize; i += 2, pt1++, pt2++) {
        output[i] = nums[pt1];
        output[i + 1] = nums[pt2];
    }

    return output;
}