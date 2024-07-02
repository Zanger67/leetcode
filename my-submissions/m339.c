/**
 * *********************************************************************
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * *********************************************************************
 *
 * // Initializes an empty nested list and return a reference to the nested integer.
 * struct NestedInteger *NestedIntegerInit();
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * bool NestedIntegerIsInteger(struct NestedInteger *);
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * int NestedIntegerGetInteger(struct NestedInteger *);
 *
 * // Set this NestedInteger to hold a single integer.
 * void NestedIntegerSetInteger(struct NestedInteger *ni, int value);
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 * void NestedIntegerAdd(struct NestedInteger *ni, struct NestedInteger *elem);
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The result is undefined if this NestedInteger holds a single integer
 * struct NestedInteger **NestedIntegerGetList(struct NestedInteger *);
 *
 * // Return the nested list's size that this NestedInteger holds, if it holds a nested list
 * // The result is undefined if this NestedInteger holds a single integer
 * int NestedIntegerGetListSize(struct NestedInteger *);
 * };
 */
int helper(struct NestedInteger* curr, int multiplier) {
    if (NestedIntegerIsInteger(curr)) {
        return multiplier * NestedIntegerGetInteger(curr);
    }
    
    int lstSize = NestedIntegerGetListSize(curr);
    struct NestedInteger** lst = NestedIntegerGetList(curr);
    
    int output = 0;
    for (int i = 0; i < lstSize; i++) {
        output += helper(lst[i], multiplier + 1);
    }

    return output;
}

int depthSum(struct NestedInteger** nestedList, int nestedListSize) {
    int output = 0;
    for (int i = 0; i < nestedListSize; i++) {
        output += helper(nestedList[i], 1);
    }
    return output;
}