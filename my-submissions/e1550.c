bool threeConsecutiveOdds(int* arr, int arrSize) {
    for (int i = 2; i < arrSize; i++) {
        if (arr[i] % 2 == arr[i - 1] % 2 && 
            arr[i - 1] % 2 == arr[i - 2] % 2 && 
            arr[i - 2] % 2 == 1)
            return true;
    }
    return false;
}