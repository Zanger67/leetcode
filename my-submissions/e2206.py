class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        vals = set()

        for num in nums :
            if num in vals :
                vals.remove(num)
            else :
                vals.add(num)

        return len(vals) == 0