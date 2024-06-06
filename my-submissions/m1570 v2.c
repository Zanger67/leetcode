// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/


typedef struct {
    int* nums;
    int numsSize;
} SparseVector;


SparseVector* sparseVectorCreate(int* nums, int numsSize) {
    
    // number of values to store
    int newNumSize = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i]) {
            newNumSize++;
        }
    }

    // storing the values
    SparseVector* data = malloc(sizeof(SparseVector));
    data->nums = (int*) malloc(sizeof(int) * newNumSize * 2);
    data->numsSize = newNumSize;
    
    for (int i = 0, currPointer = 0; i < numsSize; i++) {
        if (nums[i]) {
            data->nums[currPointer] = i;
            data->nums[currPointer + 1] = nums[i];
            currPointer += 2;
        }
    }

    return data;
}

// Return the dotProduct of two sparse vectors
int sparseVectordotProduct(SparseVector* obj, SparseVector* vec) {
    int output = 0;
    for (int i = 0, j = 0; i < 2 * obj->numsSize && j < 2 * vec->numsSize;) {
        if (obj->nums[i] < vec->nums[j]) {
            i += 2;
        } else if (obj->nums[i] > vec->nums[j]) {
            j += 2;
        } else {
            output += obj->nums[i + 1] * vec->nums[j + 1];
            i += 2;
            j += 2;
        }
    }

    return output;
}

/**
 * Your SparseVector struct will be instantiated and called as such:
 * SparseVector* v1 = sparseVectorCreate(nums1, nums1Size);
 * SparseVector* v2 = sparseVectorCreate(nums2, nums2Size);
 * int ans = sparseVectordotProduct(v1, v2);
*/