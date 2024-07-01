/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* output = (int*) malloc(sizeof(int) * wordsSize);
    int outputPtr = 0;

    for (int i = 0; i < wordsSize; i++) {
        int temp = 0;
        while (words[i][temp]) {
            if (words[i][temp] == x) {
                output[outputPtr] = i;
                outputPtr++;
                break;
            }

            temp++;
        }
    }

    *returnSize = outputPtr;
    return output;
}