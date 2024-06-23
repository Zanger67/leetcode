class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = deque(sorted(piles))

        output: int = 0
        while piles :
            piles.pop()
            output += piles.pop()
            piles.popleft()

        return output