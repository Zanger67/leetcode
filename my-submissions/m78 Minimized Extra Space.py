# https://leetcode.com/problems/subsets/description/

# Minimizes the number of array copies formed to consistently hit 97% space efficiency
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(currentList: List[int], remaining: List[int], add):
            if add :
                output.append(currentList.copy())
            
            if len(remaining) == 0 :
                return

            nextTerm = remaining.pop()
            helper(currentList, remaining, False)
            currentList.append(nextTerm)
            helper(currentList, remaining, True)
            remaining.append(currentList.pop())
            

        helper([], nums, True)

        return output