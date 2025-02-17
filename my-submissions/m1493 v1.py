class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ones = [0]

        while nums :
            curr = nums.pop()
            if curr and ones and ones[-1] :
                ones[-1] += 1
                continue

            if curr :
                ones.append(1)
                continue

            ones.append(0)

        ones.append(0)

        if len(ones) == 3 :
            return max(0, sum(ones) - 1)

        maxx = 0
        for i in range(1, len(ones) - 1) :
            maxx = max(maxx, ones[i - 1] + ones[i] + ones[i + 1])

        return maxx
