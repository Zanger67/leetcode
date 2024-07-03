#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        def helper(curr: List[int], currOutput: List[int], add: bool) -> None :
            if add :
                output.append(currOutput.copy())
            if not curr :
                return

            # Count instances
            counter = 1
            val = curr.pop()

            while curr and curr[-1] == val :
                counter += 1
                curr.pop()

            # If none added, don't readd output since it already exists
            helper(curr, currOutput, False)
            currOutput.append(val)

            # Iterate through adding 1, 2, 3, ...etc. cases
            for i in range(1, counter) :
                helper(curr, currOutput, True)
                currOutput.append(val)

            helper(curr, currOutput, True)

            # Readd and repop
            for i in range(counter) :
                currOutput.pop()
                curr.append(val)

        helper(nums, [], True)
        return output
# @lc code=end

