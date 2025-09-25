class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        curr = triangle[-1]
        for r in range(len(triangle) - 2, -1, -1) :
            curr = [triangle[r][i] + min(curr[i:i+2]) for i in range(len(triangle[r]))]
        return curr[0]