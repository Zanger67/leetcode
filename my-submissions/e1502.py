# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr) - 2) :
            if not arr[i] - arr[i + 1] == arr[i + 1] - arr[i + 2] :
                return False

        return True