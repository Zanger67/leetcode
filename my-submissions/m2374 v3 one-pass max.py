class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        nodeSums = [0] * len(edges)

        maxx = 0
        indx = 0
        for i, targetEdge in enumerate(edges) :
            nodeSums[targetEdge] += i
            if maxx < nodeSums[targetEdge] or (maxx == nodeSums[targetEdge] and indx > targetEdge):
                maxx = nodeSums[targetEdge]
                indx = targetEdge
        
        return indx