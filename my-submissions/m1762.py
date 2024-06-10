# https://leetcode.com/problems/buildings-with-an-ocean-view/description/


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        output = []
        currentMax = -inf
        for i in range(len(heights) - 1, -1, -1) :
            if heights[i] > currentMax :
                output.append(i)
                currentMax = heights[i]

        return reversed(output)