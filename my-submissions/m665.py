class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)) :
            if nums[i - 1] > nums[i] :
                # is last val causing so we don't have to "reconnect"
                if i + 1 >= len(nums) :
                    return True

                # if right half has issue, we have more than 1 edit confirmed
                for j in range(i + 1, len(nums)) :
                    if nums[j - 1] > nums[j] :
                        return False
                
                # if issue is the starting value, we don't have to check the two sides
                if i == 1 :
                    return True

                # if deleting one of the two values will allow the two halves to connect
                # so that they're non-decending, we good
                return (nums[i - 2] <= nums[i]) or (nums[i - 1] <= nums[i + 1])

        # by default already non-decending
        return True