class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = [0]
        consec_ones = 0

        for num in nums :
            if num == 0 :
                if consec_ones :
                    ones.append(consec_ones)
                ones.append((consec_ones := 0))
            else :
                consec_ones += 1
        ones.append(consec_ones)

        return max([sum(ones[x - 1:x+2]) + abs(min(ones[x], 1) - 1)
                    for x in range(1, len(ones) - 1)] + ones)