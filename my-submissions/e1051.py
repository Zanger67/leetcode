class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        return len(heights) - [heights[x] - sortedHeights[x] for x in range(len(heights))].count(0)