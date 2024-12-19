class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        return [prices[i] - min([(indx, discount) for indx, discount in enumerate(prices[i + 1 :]) if discount <= prices[i]] + [(inf, 0)], key=lambda x: x[0])[1] for i in range(len(prices))]
