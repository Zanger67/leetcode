int comp(const void* a, const void* b) {
    return *((int*) a) - *((int*) b);
}

int maxIceCream(int* costs, int costsSize, int coins) {
    qsort(costs, costsSize, sizeof(int), comp);
    
    for (int i = 0; i < costsSize; i++) {
        if (coins < costs[i])
            return i;
        coins -= costs[i];
    }

    return costsSize;
}