// https://leetcode.com/problems/counting-elements/description/

// Oddly stated question
/* Wasnt sure if they wanted the repeat values to be like n*m, min(n,m), or whatnot
 * In the end tinkering found that what the test cases search for is just n as in n
 * can pair to any m values but if n=1, no matter how many m's there are n can only
 * pair to one.
 */

int countElements(int* arr, int arrSize) {
    short* temp = malloc(sizeof(short) * 1001);
    for (int i = 0; i < 1001; i++) {
        temp[i] = 0;
    }

    for (int i = 0; i < arrSize; i++) {
        temp[arr[i]]++;
    }

    int output = 0;
    for (int i = 0; i < 1000; i++) {
        if (temp[i] && temp[i + 1]) {
            output += temp[i];
        }
    }

    free(temp);
    return output;
}