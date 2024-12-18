class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = [-1] * len(prices)

        for i in range(len(prices) - 1, -1, -1) :
            price = prices[i]
            maxx = 0
            for disc in prices[i + 1:] :
                if disc > price :
                    continue
                maxx = disc
                break
            output[i] = price - maxx

        return output
