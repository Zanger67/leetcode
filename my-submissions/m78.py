class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(currentList: List[int], remaining: List[int], add):
            if add :
                output.append(currentList)
            
            if len(remaining) == 0 :
                return

            nextTerm = remaining.pop()
            remainingCopy1 = remaining.copy()
            remainingCopy2 = remaining.copy()

            helper(currentList, remainingCopy1, False)
            newCurrentList = currentList.copy()
            newCurrentList.append(nextTerm)
            helper(newCurrentList, remainingCopy2, True)

        helper([], nums, True)

        return output