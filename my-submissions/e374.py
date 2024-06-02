# https://leetcode.com/problems/guess-number-higher-or-lower/description/


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left < right :
            mid = (left + right) // 2
            gs = guess(mid)

            match gs :
                case -1 :
                    right = mid - 1
                case 1 :
                    left = mid + 1
                case 0 :
                    return mid
        
        return left