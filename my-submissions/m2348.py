class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        output = 0
        cnt = 0
        for i in range(len(nums)) :
            if nums[i] != 0 :
                output += cnt * (cnt + 1) // 2
                cnt = 0
                continue
            cnt += 1
        output += cnt * (cnt + 1) // 2
        return output
