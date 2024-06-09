# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/?envType=daily-question&envId=2024-06-09

# Weirdly slow hm --> ~5% runtime consistely


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # prefix sum of remainders
        nums[0] %= k
        for i in range(1, len(nums)) :
            nums[i] = (nums[i] + nums[i - 1]) % k
        
        repeatRemainders = Counter(nums)
        output = repeatRemainders.get(0, 0)

        for key in repeatRemainders.keys() :
            if repeatRemainders.get(key) >= 2 :
                output += comb(repeatRemainders.get(key), 2)

        return output