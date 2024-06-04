# [40/50% region]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        numSlides = len(nums) - k + 1
        output = [0] * numSlides

        # indices of values to use
        dequeueuee = deque()

        # initializing the first bit of space with deque index records
        for i in range(0, k - 1) :
            if not dequeueuee :
                dequeueuee.append(i) 
                continue
            while dequeueuee and nums[dequeueuee[0]] <= nums[i] : 
                dequeueuee.popleft()
            dequeueuee.appendleft(i)
        
        # rest of it lol
        for i in range(k - 1, len(nums)) :
            while dequeueuee and dequeueuee[-1] < i - k + 1 :
                dequeueuee.pop()
            while dequeueuee and (dequeueuee[0] < i - k + 1 or nums[dequeueuee[0]] <= nums[i]) :
                dequeueuee.popleft()
            dequeueuee.appendleft(i)
            output[i - k + 1] = nums[dequeueuee[-1]]
        
        return output