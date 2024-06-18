class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        nodeSums = defaultdict(int)

        for i, targetEdge in enumerate(edges) :
            nodeSums[targetEdge] += i

        return max(nodeSums.keys(), key=lambda x : (nodeSums[x], -x))