# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Primary issue is that with this method, if the histogram is increasing only, then
# there are a LOT of checks and loops...
# Could reverse but it's a matter of knowing whether it's primarily increasing or decreasing.


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ''' This makes it work but I do think this would be cheating. It does improve 
            runtime for *this* version in order to make it barely satisfy the necessary runtime
            and is in theory valid but again, I believe there's a better solution I need to find.

            The reversal if the histogram is primarily increasing is a good way to reduce runtime since
            my algorithm is optimized for a decreasing histogram, but it overall does little for a 
            relatively uniform case. It simply helps counteract the edge case for what I designed my
            algo after.

            Runtime ends up being in the 5% percentile.
        '''
        
        counter = 0
        for i in range(1, len(heights)) :
            if heights[i] >= heights[i - 1] :
                counter += 1
        
        if counter > len(heights) // 2 :
            heights = list(reversed(heights))
        
        prevMaxes = []

        maxArea = 0
        for i, height in enumerate(heights) :
            lastIndx = i
            while prevMaxes and prevMaxes[-1][1] >= height :
                lastIndx = prevMaxes.pop()[0]
        
            if prevMaxes and prevMaxes[-1][0] - lastIndx > height - prevMaxes[-1][1] :
                continue
            prevMaxes.append((lastIndx, height))
            
            for prevMax in prevMaxes :
                maxArea = max((i - prevMax[0] + 1) * prevMax[1], maxArea)
            
        return maxArea
