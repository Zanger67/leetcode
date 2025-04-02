class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_n, max_dif, output = 0, 0, 0
        return max([
            output := (max(output, max_dif * n), 
                       max_n := max(max_n, n), 
                       max_dif := max(max_dif, max_n - n))[0] 
            for n in nums
        ])