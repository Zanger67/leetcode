class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        hs = {i: nums[i] for i in range(len(nums))}

        maxx = 0
        while hs :
            curr = random.choice(list(hs.keys()))
            lenth = 0

            while curr in hs :
                lenth += 1
                temp = hs.get(curr)
                hs.pop(curr)
                curr = temp
            maxx = max(maxx, lenth)
            
        return maxx