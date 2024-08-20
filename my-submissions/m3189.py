class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        remainingRows = set(range(len(rooks)))
        remainingCols = remainingRows.copy()
        extraRows = []
        extraCols = []

        for x, y in rooks :
            if x in remainingRows :
                remainingRows.remove(x)
            else :
                heapq.heappush(extraRows, x)

            if y in remainingCols :
                remainingCols.remove(y)
            else :
                heapq.heappush(extraCols, y)

        remainingRows = sorted(list(remainingRows), reverse=True)
        remainingCols = sorted(list(remainingCols), reverse=True)
        output = 0

        while remainingRows :
            output += abs(remainingRows.pop() - heapq.heappop(extraRows))
        while remainingCols :
            output += abs(remainingCols.pop() - heapq.heappop(extraCols))


        return output
