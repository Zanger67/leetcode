int compHelper(const void* a, const void* b) {
    return *((int*) a) - *((int*) b);
}

int minProductSum(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int output = 0;

    qsort(nums1, nums1Size, sizeof(int), compHelper);
    qsort(nums2, nums2Size, sizeof(int), compHelper);

    for (int i = 0; i < nums1Size; i++) {
        output += nums1[i] * nums2[nums2Size - i - 1];
    }

    return output;

}