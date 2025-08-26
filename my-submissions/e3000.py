class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return prod(max(dimensions, key=(lambda x: (sqrt(x[0] ** 2 + x[1] ** 2), prod(x)))))