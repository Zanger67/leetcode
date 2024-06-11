// https://leetcode.com/problems/height-checker/description/


int compareHelper(const void* a, const void* b) {
    return *((int*) a) - *((int*) b);
}
int heightChecker(int* heights, int heightsSize) {
    int sortedHeights[heightsSize];
    for (int i = 0; i < heightsSize; i++) {
        sortedHeights[i] = heights[i];
    }

    qsort(sortedHeights, heightsSize, sizeof(int), compareHelper);

    int counter = 0;
    for (int i = 0; i < heightsSize; i++) {
        if (sortedHeights[i] != heights[i])
            counter++;
    }

    return counter;
}