// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/

int compareHelper(const void* one, const void* two) {
    return *((int *) one) - *((int *) two);
}

bool canMakeArithmeticProgression(int* arr, int arrSize) {
    qsort(arr, arrSize, sizeof(int), compareHelper);

    for (int i = 0; i < arrSize - 2; i++) {
        if (!(arr[i] - arr[i + 1] == arr[i + 1] - arr[i + 2])) {
            return false;
        }
    }
    return true;
}