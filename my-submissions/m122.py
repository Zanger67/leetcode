class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(filter(lambda x: x > 0, [y - x for x, y in zip(prices[:-1], prices[1:])]))