class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        curr = []
        output = 0
        indx = 0

        for num in nums :
            if curr and curr[-1] >= num :
                curr = []
            curr.append(num)
            output += len(curr)
            indx += 1

        return output