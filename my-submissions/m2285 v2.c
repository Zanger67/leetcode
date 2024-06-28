int compare(const void* a, const void* b) {
    return *((int*) a) - *((int*) b);
}

long long maximumImportance(int n, int** roads, int roadsSize, int* roadsColSize) {
    int cnt[n];
        memset(&cnt, 0, n * sizeof(int));

        for (int i = 0; i < roadsSize; i++) {
            cnt[roads[i][0]]++;
            cnt[roads[i][1]]++;
        }

        qsort(cnt, n, sizeof(int), compare);

        long long output = 0;
        for (int i = n; i > 0 && cnt[i - 1] > 0; i--) {
            output += (long long) i * (long long) cnt[i - 1];
        }
        return output;
}
