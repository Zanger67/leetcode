class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        minn, maxx = 0, 0
        curr = 0

        for dif in differences :
            curr += dif
            minn, maxx = min(minn, curr), max(maxx, curr)

        return max(0, (upper - lower + 1) - (maxx - minn))