class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bars = 0
        costs.sort(reverse=True)

        while costs :
            if coins < costs[-1] :
                return bars
            bars += 1
            coins -= costs.pop()

        return bars