// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/


int compareHelper(const void* one, const void* two) {
    return *((int *) one) - *((int *) two);
}

bool canBeEqual(int* target, int targetSize, int* arr, int arrSize) {
    if (!(targetSize == arrSize)) {
        return false;
    }

    qsort(arr, arrSize, sizeof(int), compareHelper);
    qsort(target, targetSize, sizeof(int), compareHelper);
    
    for (int i = 0; i < arrSize; i++) {
        if (!(arr[i] == target[i])) {
            return false;
        }
    }
    return true;
}