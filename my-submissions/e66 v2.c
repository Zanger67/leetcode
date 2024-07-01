// Version that doesn't deal with the free() issue but uses some more memory in the process during shifting :v

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int* output = (int*) malloc(sizeof(int) * digitsSize);

    bool carry = true;
    for (int i = digitsSize - 1; i >= 0; i--) {
        int temp = digits[i] + ((carry) ? 1 : 0);
        if (temp > 9) {
            carry = true;
            output[i] = (temp - 10);
        } else {
            carry = false;
            output[i] = temp;
        }
    }

    *returnSize = (carry) ? digitsSize + 1 : digitsSize;

    if (!carry) {
        return output;
    }

    int* output2 = (int*) malloc(sizeof(int) * (1 + digitsSize));
    output2[0] = 1;
    memcpy(output2 + 1, output, sizeof(int) * digitsSize); 
    free(output);
    return output2;

}