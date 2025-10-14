class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        indx = 0
        continues = False
        while indx <= len(nums) - 2 * k :
            works = True
            if not continues :
                for i in range(indx + 1, indx + k) :
                    if nums[i] <= nums[i - 1] :
                        indx, works = i, False
                        break
                if not works :
                    continue

            works = True
            continues = bool(nums[indx + k - 1] < nums[indx + k])
            for i in range(indx + k + 1, indx + 2 * k) :
                if nums[i] <= nums[i - 1] :
                    works = False
                    indx = i - k if continues else i
                    break

            if works :
                return True

        return False