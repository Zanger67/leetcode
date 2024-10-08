class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1 :
            return nums.copy()

        # Setting up the left and right half heaps
        rightMinHeap = nums[:k - 1]
        heapq.heapify(rightMinHeap)
        leftMaxHeap = []

        for i in range((k - 1) // 2) :
            heapq.heappush(leftMaxHeap, -heapq.heappop(rightMinHeap))

        # Counters to track the values (1 for the combined two heaps; 1 for the window)
        # This lets us know whether to pop the middle values
        # intended = window counter
        # current  = heap counter
        intended = Counter(nums[:k-1])
        current = intended.copy()

        output = []

        # If even k value, we need to take averages
        medianSharedByTwo = (k % 2 == 0)


        # Loop
        for i, v in enumerate(nums[k - 1:]) :
            # add current val
            if v > rightMinHeap[0] :
                heapq.heappush(leftMaxHeap, -heapq.heappushpop(rightMinHeap, v))
            else :
                heapq.heappush(leftMaxHeap, -v)

            # clean up any values that are no longer within the window
            while leftMaxHeap and intended[-leftMaxHeap[0]] != current[-leftMaxHeap[0]] :
                current[-leftMaxHeap[0]] -= 1
                heapq.heappop(leftMaxHeap)

            while rightMinHeap and intended[rightMinHeap[0]] != current[rightMinHeap[0]] :
                current[rightMinHeap[0]] -= 1
                heapq.heappop(rightMinHeap)

            # Add median
            output.append(-leftMaxHeap[0] if not medianSharedByTwo else (-leftMaxHeap[0] + rightMinHeap[0]) / 2)

            # Increase this value in our counters since we just added it
            intended[v] += 1
            current[v] += 1

            # Remove the last/leftmost value aka the value that the window is leaving
            remVal = nums[i]
            # Remove from window counter
            intended[remVal] -= 1

            # Check cases
            if remVal == -leftMaxHeap[0] :      # If is left val, just remove it
                heapq.heappop(leftMaxHeap)
                current[remVal] -= 1
            elif remVal == rightMinHeap[0] :    # If is right val, remove it and shift 
                                                # the left peek value over to keep the 
                                                # left ready to add (keep it lighter by default)
                heapq.heappop(rightMinHeap)
                heapq.heappush(rightMinHeap, -heapq.heappop(leftMaxHeap))
                current[remVal] -= 1
            elif remVal > rightMinHeap[0] :     # If it's on the right half, balance it out by 
                                                # shifting a value but don't bother removing it 
                                                # properly since removal operations are expensive
                heapq.heappush(rightMinHeap, -heapq.heappop(leftMaxHeap))
            elif remVal < -leftMaxHeap[0] :     # Ignore this case since it doesn't affect our 
                                                # heap balance
                pass

        return output
