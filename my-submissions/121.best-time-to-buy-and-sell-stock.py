#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        maxxPrice = prices[-1]
        for price in reversed(prices) :
            if price > maxxPrice :
                maxxPrice = price
            elif maxxPrice - price > output :
                output = maxxPrice - price
        return output
# @lc code=end

