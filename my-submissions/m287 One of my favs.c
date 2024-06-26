/**
 * Thought process
 * Each value will point to another index, and that
 * to another and another 
 * 
 * We're given values [1, n] inclusive of length n+1 so
 * XORing should be (1^2^...^n) ^ repeatVal
 * 
 */


int findDuplicate(int* nums, int numsSize) {
    int fast = nums[0];
    int slow = nums[0];

    do {
        fast = nums[nums[fast]];
        slow = nums[slow];
    } while (fast != slow);

    slow = nums[0];
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[fast];
    }

    return fast;

}