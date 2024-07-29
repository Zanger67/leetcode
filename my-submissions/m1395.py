class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # No need for "equal" case since all rating values are UNIQUE
        countValsSmaller = []
        countValsGreater = []

        # NOTE: Calculating how many values are less than, on the left
        # O(n^2)
        # Stores negatives for MAXHEAP
        valsSmaller = []
        # Stores positives for MINHEAP
        otherVals = []
        for i, r in enumerate(rating) :
            while valsSmaller and -valsSmaller[0] >= r :
                heapq.heappush(otherVals, -heapq.heappop(valsSmaller))
            while otherVals and otherVals[0] < r :
                heapq.heappush(valsSmaller, -heapq.heappop(otherVals))

            countValsSmaller.append(len(valsSmaller))
            heapq.heappush(otherVals, r)

        del valsSmaller
        del otherVals

        # NOTE: Calculating how many values are greater than, on the right
        # O(n^2)
        # Stores positives for MINHEAP
        valsGreater = []
        # Stores negatives for MAXHEAP
        otherVals = []
        for i, r in enumerate(reversed(rating)) :
            while valsGreater and valsGreater[0] <= r :
                heapq.heappush(otherVals, -heapq.heappop(valsGreater))
            while otherVals and -otherVals[0] > r :
                heapq.heappush(valsGreater, -heapq.heappop(otherVals))

            countValsGreater.append(len(valsGreater))
            heapq.heappush(otherVals, -r)

        countValsGreater.reverse()

        del valsGreater
        del otherVals

        # Iterating through the indices to calculate the final total
        # O(n)
        counter = 0
        for i in range(1, len(rating) - 1) :
            # Internal calculation to find the missing 2 values
            # since if they're unique, then #total - #smaller = #greater
            # Done here instead of above to save on space usage by half.
            smallerLeft = countValsSmaller[i]
            smallerRight = len(rating) - 1 - i - countValsGreater[i]
            greaterLeft = i - countValsSmaller[i]
            greaterRight = countValsGreater[i]

            counter += smallerLeft * greaterRight + smallerRight * greaterLeft

        return counter