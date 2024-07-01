''' Idea
    Go through each adjacent pairing until you find an increasing pairing
    
    If found, check to see if it's the last value causing the decrease.
        Return True if it is cause we can just change to be infinity or starmap
        
        Iterate through the values to the right of the issue section to see if
        there's another issue. If there is, return False cause we're only alowed
        to modify one value.

        Return True if the problem value is the first pairing, since we can just
        nums[0] = -inf to solve it

        Return True if by deleting the value or by deleting the value before, the 
        two halves connect and are non-decreasing.

        It's an OR cause it could be smt like [1, 2, 5, 7, 3, 5, 6] where (7, 3) is
        the flagged pair but (5, 3) by deleting 7 doesn't work and (7, 5) by deleting
        3 also doesn't work

    If no increasing pair found at all, return true
'''

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