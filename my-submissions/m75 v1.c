void sortColors(int* nums, int numsSize) {
    int indx = 0;
    int currentRed = numsSize - 1;

    while (indx < currentRed) {
        while (indx < currentRed && nums[indx] == 0) {
            indx++;
        }
        while (indx < currentRed && nums[currentRed] != 0) {
            currentRed--;
        }
        int holder = nums[indx];
        nums[indx] = nums[currentRed];
        nums[currentRed] = holder;        
    }

    int currentWhite = numsSize - 1;
    while (indx < currentWhite) {
        while (indx < currentWhite && nums[indx] == 1) {
            indx++;
        }
        while (indx < currentWhite && nums[currentWhite] != 1) {
            currentWhite--;
        }
        int holder = nums[indx];
        nums[indx] = nums[currentWhite];
        nums[currentWhite] = holder;        
    }
}