// https://leetcode.com/problems/plus-one/?envType=problem-list-v2&envId=r9zp3ka3

// Beats 100% but this notably might have free() issues with output if it has a carry on the last digit :l

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int* output = (int*) malloc(sizeof(int) * (digitsSize + 1));

    bool carry = true;
    for (int i = digitsSize - 1; i >= 0; i--) {
        int temp = digits[i] + ((carry) ? 1 : 0);
        if (temp > 9) {
            carry = true;
            output[i + 1] = (temp - 10);
        } else {
            carry = false;
            output[i + 1] = temp;
        }
    }

    *returnSize = (carry) ? digitsSize + 1 : digitsSize;

    if (carry) {
        output[0] = 1;
        return output;
    } else {
        return output + 1;
    }
}