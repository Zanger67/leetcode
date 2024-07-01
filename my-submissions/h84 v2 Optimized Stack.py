# V2 that's *slightly* better but still not the greatest

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prevMaxes = []

        maxArea = 0
        for i, height in enumerate(heights) :
            lastIndx = i
            while prevMaxes and prevMaxes[-1][1] > height :
                maxArea = max(maxArea, (i - prevMaxes[-1][0]) * prevMaxes[-1][1])
                lastIndx = prevMaxes.pop()[0]
            prevMaxes.append((lastIndx, height))
            maxArea = max((i - lastIndx + 1) * height, maxArea)

        while prevMaxes :
            maxArea = max((len(heights) - prevMaxes[-1][0]) * prevMaxes[-1][1], maxArea)
            prevMaxes.pop()

        return maxArea
