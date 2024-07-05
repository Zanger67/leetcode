class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right :
            mid = (left + right) // 2
            if nums[mid - 1] != nums[mid] != nums[mid + 1] :
                return nums[mid]

            if mid % 2 == 1 :
                if nums[mid] == nums[mid - 1] :
                    # is to right 
                    left = mid + 1
                else :
                    right = mid - 1
            elif nums[mid] == nums[mid + 1] :
                left = mid + 1
            else :
                right = mid - 1
        
        return nums[left]