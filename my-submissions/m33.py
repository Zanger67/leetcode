class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # find rotation amount via bin search
        left, right = 0, n - 1
        while left < right - 1 :
            # get mid index and val
            mid = (left + right) // 2
            val = nums[mid]

            # ret if found
            if target == val :
                return mid

            # shift
            if val < nums[left] :
                right = mid
                continue
            left = mid

        # account for no rotation
        offset = 0 if nums[right] - nums[left] > 0 else right

        # regular bin search
        left, right = offset, offset + n - 1
        while left <= right:
            mid = ((left + right) // 2)
            val = nums[mid % n]

            # found val
            if val == target :
                return mid % n

            # shift
            if target < val :
                right = mid - 1
                continue
            left = mid + 1

        return -1
