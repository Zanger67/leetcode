// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

int finalValueAfterOperations(char** operations, int operationsSize) {
    int output = 0;
    
    for (int i = 0; i < operationsSize; i++) {
        if (operations[i][1] == 43) {
            output++;
        } else {
            output--;
        }
    }
    return output;
}