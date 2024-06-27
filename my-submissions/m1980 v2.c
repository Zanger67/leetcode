char* findDifferentBinaryString(char** nums, int numsSize) {
    char* output = (char*) malloc(sizeof(char) * (numsSize + 1));

    for (int i = 0; i < numsSize; i++) {
        output[i] = (nums[i][i] == '1') ? '0' : '1';
    }
    output[numsSize] = 0;

    return output;
}