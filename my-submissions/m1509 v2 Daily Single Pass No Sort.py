# .sort() for 4 values would be minimal and a constant max 
# cost. This just simplified the typing process but could easily
# be changed for better efficiency. It's essentially a single 
# iteration of insertion sort.

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4 :
            return 0
        
        top4 = sorted(nums[:4], reverse=True)
        bot4 = sorted(nums[:4])

        for num in nums[4:] :
            if num > top4[3] :
                top4.append(num)
                top4.sort(reverse=True)
                top4.pop()
            if num < bot4[3] :
                bot4.append(num)
                bot4.sort()
                bot4.pop()

        return min([top4[i] - bot4[3 - i] for i in range(4)])
