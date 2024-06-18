class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        nodeSums = [0] * len(edges)

        for i, targetEdge in enumerate(edges) :
            nodeSums[targetEdge] += i

        return max([i for i in range(len(edges))], key=lambda x: (nodeSums[x], -x))