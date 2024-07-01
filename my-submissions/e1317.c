/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

bool containsZero(int n) {
    while (n > 0) {
        if (n % 10 == 0) {
            return true;
        }
        n /= 10;
    }

    return false;
}

int* getNoZeroIntegers(int n, int* returnSize) {
    int* output = (int*) malloc(sizeof(int) * 2);

    for (int i = 1; i < n; i++) {
        if (!containsZero(n - i) && !containsZero(i)) {
            output[0] = n - i;
            output[1] = i;
            break; 
        }
    }
    
    *returnSize = 2;
    return output;
    
}