# Extremly low space efficiency but it passes soooo (5% margine consistently)
# Runtime is similarly in the [0,25] region

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        numSlides = len(nums) - k + 1
        output = [0] * numSlides

        pastVals = []

        # initialization of first k values
        for i in range(k):
            heapq.heappush(pastVals, (-1 * nums[i], i))
            output[0] = pastVals[0][0] * -1
            

        for i in range(k, len(nums)) :
            heapq.heappush(pastVals, (-1 * nums[i], i))

            while (pastVals[0][1] < i - k + 1) :
                heapq.heappop(pastVals)

            output[i - k + 1] = -1 * pastVals[0][0]


        return output