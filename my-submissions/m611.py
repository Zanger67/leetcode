class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        self.pastLeftRight = set()
        self.nums = nums
        self.nums.sort()

        return self.helper(0, len(nums) - 1, len(nums) - 1)
    
    def helper(self, left: int, right: int, prevPoint: int) -> int:
        if (not right - 1 > left) : # can't let them cross and we need to res a val for mid
            return 0 

        if ((left, right) in self.pastLeftRight) : #-1 to account for the middle value
            return 0
        
        self.pastLeftRight.add((left,right))
        rightMinusLefts = self.nums[right] - self.nums[left]

        curr = (left + right) // 2
        # curr = prevPoint
        currLeft = left
        currRight = min(prevPoint, right)
        while (currLeft < currRight) : # we want to move LEFT as much as possible
            if (rightMinusLefts - self.nums[curr] >= 0) : # note we cannot check for exactness easily due to us binsearching for "this works" rather than "this is"
                currLeft = curr + 1
                curr = (currLeft + currRight) // 2
            else :
                currRight = curr # we need to keep at least the rightmost working
                curr = (currLeft + currRight) // 2

                if (curr <= left) :
                    curr = currRight
                    break

        retVal = right - curr

        # if right is decreasing, then bias will be for point moving left -- point cannot be more right than previous
        # if left is increasing, then bias will bias to the left too...

        return retVal + self.helper(left + 1, right, curr + 1) + self.helper(left, right - 1, curr + 1)
