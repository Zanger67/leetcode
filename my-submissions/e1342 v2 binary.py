class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0 :
            return 0
        bin_str = bin(num)[3:]
        ones = bin_str.count('1')
        return 1 + 2 * ones + len(bin_str) - ones