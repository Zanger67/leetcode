class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 0 if (a := abs(x - z)) == (b := abs(y - z)) else 1 if a < b else 2