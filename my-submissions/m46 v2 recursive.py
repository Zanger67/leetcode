# https://leetcode.com/problems/permutations/

# Since using itertools defeats the purpose of this quesiton lol

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.outs = []

        def helper(current: List[int], remainingNums: set()) -> None :
            if not remainingNums :
                self.outs.append(current.copy())
                return

            nextRemainingNums = remainingNums.copy()
            for i in remainingNums :
                current.append(i)
                nextRemainingNums.remove(i)
                helper(current, nextRemainingNums)
                nextRemainingNums.add(current.pop())
            
        helper([], set(nums))
        return self.outs
        