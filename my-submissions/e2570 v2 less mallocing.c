// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** mergeArrays(int** nums1, int nums1Size, int* nums1ColSize, int** nums2, int nums2Size, int* nums2ColSize, int* returnSize, int** returnColumnSizes){
    // To act in effect as a hashmap of size 1001 so we can just place 
    // the vals here temporarily
    int output[2 * 1001] = {0};

    // Going through each of the input vals
    int numValsInOutput = 0;

    for (int i = 0; i < nums1Size; i++) {
        if (output[nums1[i][0] * 2] == 0) {
            output[nums1[i][0] * 2] = nums1[i][0];
            output[nums1[i][0] * 2 + 1] = nums1[i][1];
            numValsInOutput++;
        } else {
            output[nums1[i][0] * 2 + 1] += nums1[i][1];
        }
    }

    for (int i = 0; i < nums2Size; i++) {
        if (output[nums2[i][0] * 2] == 0) {
            output[nums2[i][0] * 2] = nums2[i][0];
            output[nums2[i][0] * 2 + 1] = nums2[i][1];
            numValsInOutput++;
        } else {
            output[nums2[i][0] * 2 + 1] += nums2[i][1];
        }
    }

    // Mallocing and filling the actual output space
    int** realOutput = (int**) malloc(sizeof(int*) * numValsInOutput);
    *returnSize = numValsInOutput;
    *returnColumnSizes = (int*) malloc(sizeof(int) * numValsInOutput);

    int pos = 0;
    int outputPos = 0;
    while (pos < numValsInOutput) {
        if (output[outputPos] != 0) {
            realOutput[pos] = (int*) malloc(sizeof(int) * 2);
            realOutput[pos][0] = output[outputPos];
            realOutput[pos][1] = output[outputPos + 1];
            (*returnColumnSizes)[pos] = 2;
            pos++;
        }
        outputPos += 2;
    }

    return realOutput;
}