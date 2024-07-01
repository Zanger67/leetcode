// Brute forcey based on constraints but eh twas simpler
// Plus consistently 100% runtime with typically good % memory

int sumOfUnique(int* nums, int numsSize) {
    short ref[101] = {0};

    int sum = 0;
    for (int i = 0; i < numsSize; i++) {
        ref[nums[i]]++;
    }

    int output = 0;
    for (int i = 0; i < 101; i++) {
        if (ref[i] == 1) {
            output += i;
        }
    }
    return output;
}